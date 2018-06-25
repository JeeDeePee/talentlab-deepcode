import random

from graphene import relay
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
import graphene
from .models import Module, Unit, Category


class UnitNode(DjangoObjectType):
    pk = graphene.Int()

    def resolve_pk(self, *args, **kwargs):
        return self.id

    class Meta:
        model = Unit
        only_fields = [
            'slug', 'title', 'teaser', 'type', 'count', 'duration'
        ]
        filter_fields = {
            'slug': ['exact', 'icontains', 'in'],
            'title': ['exact', 'icontains', 'in'],
        }

        interfaces = (relay.Node,)


class ModuleNode(DjangoObjectType):
    pk = graphene.Int()
    tools = graphene.JSONString()
    resources = graphene.JSONString()
    units = DjangoFilterConnectionField(UnitNode)
    hero_image = graphene.String()
    # hack to acoid circular dependency
    category = graphene.JSONString()

    class Meta:
        model = Module
        only_fields = [
            'title', 'slug', 'skill', 'description', 'teaser', 'video_id', 'video_description', 'video_thumbnail_data'
        ]
        filter_fields = {
            'slug': ['exact', 'icontains', 'in'],
            'title': ['exact', 'icontains', 'in'],
        }

        interfaces = (relay.Node,)

    def resolve_tools(self, *args, **kwargs):
        return self.tools_normalized

    def resolve_resources(self, *args, **kwargs):
        return self.resources_normalized

    def resolve_pk(self, *args, **kwargs):
        return self.id

    def resolve_hero_image(self, *args, **kwargs):
        if self.hero_image:
            return self.hero_image.file.url

    def resolve_units(self, *args, **kwargs):
        # Hack to avoid error 'Cannot combine queries on two different base models.'
        # otherweise return self.get_children().specific().live() would be the thing
        return Unit.objects.filter(id__in=self.get_children().values_list('id', flat=True)).live()

    def resolve_category(self, *args, **kwargs):
        p = self.get_parent()
        return {'title': p.title, 'slug': p.slug}


class CategoryNode(DjangoObjectType):
    pk = graphene.Int()
    modules = DjangoFilterConnectionField(ModuleNode)
    icon = graphene.String()

    def resolve_pk(self, *args, **kwargs):
        return self.id

    class Meta:
        model = Category
        only_fields = [
            'slug', 'title', 'icon'
        ]
        filter_fields = {
            'slug': ['exact', 'icontains', 'in'],
            'title': ['exact', 'icontains', 'in'],
        }

        interfaces = (relay.Node,)

    def resolve_icon(self, *args, **kwargs):
        if self.icon:
            return self.icon.file.url

    def resolve_modules(self, *args, **kwargs):
        # Hack to avoid the 'Cannot combine queries on two different base models.' error
        # otherweise return self.get_children().specific().live() would be the right thing
        return Module.objects.filter(id__in=self.get_children().values_list('id', flat=True)).live()


class ModulesQuery(object):
    categories = DjangoFilterConnectionField(CategoryNode)
    modules = DjangoFilterConnectionField(ModuleNode)
    units = DjangoFilterConnectionField(UnitNode)

    def resolve_categories(self, *args, **kwargs):
        return Category.objects.filter(**kwargs).live()

    def resolve_modules(self, *args, **kwargs):
        return Module.objects.filter(**kwargs).live()

    def resolve_units(self, *args, **kwargs):
        return Unit.objects.filter(**kwargs).live()

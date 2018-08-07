from graphene import relay
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
import graphene

from modules.models.goal import Goal
from .models import Module, Unit, Category


class UnitNode(DjangoObjectType):
    pk = graphene.Int()
    module_slug = graphene.String()
    module_title = graphene.String()
    category_slug = graphene.String()
    category_title = graphene.String()

    class Meta:
        model = Unit
        only_fields = [
            'slug', 'title', 'type', 'teaser',
            'description', 'count', 'duration', 'price',
            'competences', 'module_slug', 'module_title',
            'category_slug', 'category_title'
        ]
        filter_fields = {
            'slug': ['exact', 'icontains', 'in'],
            'title': ['exact', 'icontains', 'in'],
        }
        interfaces = (relay.Node,)

    def resolve_pk(self, *args, **kwargs):
        return self.id

    def resolve_module_slug(self, *args, **kwargs):
        p = self.get_parent()
        return p.slug

    def resolve_module_title(self, *args, **kwargs):
        p = self.get_parent()
        return p.title

    def resolve_category_slug(self, *args, **kwargs):
        p = self.get_parent().get_parent()
        return p.slug

    def resolve_category_title(self, *args, **kwargs):
        p = self.get_parent().get_parent()
        return p.title


class GoalNode(DjangoObjectType):
    pk = graphene.Int()

    class Meta:
        model = Goal
        filter_fields = {
            'text': ['exact', 'icontains', 'in'],
            'level': ['exact'],
        }
        interfaces = (relay.Node,)

    def resolve_pk(self, *args, **kwargs):
        return self.id


class ModuleNode(DjangoObjectType):
    pk = graphene.Int()
    tools = graphene.JSONString()
    resources = graphene.JSONString()
    units = DjangoFilterConnectionField(UnitNode)
    hero_image = graphene.String()
    # hack to avoid circular dependency
    category = graphene.JSONString()
    category_slug = graphene.String()
    category_name = graphene.String()

    class Meta:
        model = Module
        only_fields = [
            'title', 'slug', 'skill', 'description', 'teaser', 'video_id', 'video_description', 'video_thumbnail_data', 'goal_set'
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
        return Unit.objects.filter(id__in=self.get_child_ids()).live()

    def resolve_category(self, *args, **kwargs):
        p = self.get_parent()
        return {'title': p.title, 'slug': p.slug}

    def resolve_category_slug(self, *args, **kwargs):
        p = self.get_parent()
        return p.slug

    def resolve_category_name(self, *args, **kwargs):
        p = self.get_parent()
        return p.title


class CategoryNode(DjangoObjectType):
    pk = graphene.Int()
    modules = DjangoFilterConnectionField(ModuleNode)
    icon = graphene.String()

    class Meta:
        model = Category
        only_fields = [
            'slug', 'title', 'icon', 'competence_set'
        ]
        filter_fields = {
            'slug': ['exact', 'icontains', 'in'],
            'title': ['exact', 'icontains', 'in'],
        }
        interfaces = (relay.Node,)

    def resolve_pk(self, *args, **kwargs):
        return self.id

    def resolve_icon(self, *args, **kwargs):
        if self.icon:
            return self.icon.file.url

    def resolve_modules(self, *args, **kwargs):
        # Hack to avoid the 'Cannot combine queries on two different base models.' error
        # otherweise return self.get_children().specific().live() would be the right thing
        return Module.objects.filter(id__in=self.get_child_ids()).live()


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

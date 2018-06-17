import random

from graphene import relay
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
import graphene
from .models import Container, Unit, Category


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


class ContainerNode(DjangoObjectType):
    pk = graphene.Int()
    tools = graphene.JSONString()
    resources = graphene.JSONString()
    units = DjangoFilterConnectionField(UnitNode)
    hero_image = graphene.String()

    class Meta:
        model = Container
        only_fields = [
            'title', 'slug', 'skill', 'description', 'teaser', 'video_id', 'video_description'
        ]
        filter_fields = {
            'slug': ['exact', 'icontains', 'in'],
            'title': ['exact', 'icontains', 'in'],
        }

        interfaces = (relay.Node,)

    def resolve_tools(self, *args, **kwargs):
        return self.tools.stream_data

    def resolve_resources(self, *args, **kwargs):
        return self.resources.stream_data

    def resolve_pk(self, *args, **kwargs):
        return self.id

    def resolve_hero_image(self, *args, **kwargs):
        if self.hero_image:
            return self.icon.hero_image.url

    def resolve_units(self, *args, **kwargs):
        # What an ugly hack to avoid error 'Cannot combine queries on two different base models.'
        # otherweise return self.get_children().specific().live() would be the thing
        return Unit.objects.filter(id__in=[c.id for c in self.get_children()]).live()


class CategoryNode(DjangoObjectType):
    pk = graphene.Int()
    containers = DjangoFilterConnectionField(ContainerNode)
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

    def resolve_container(self, *args, **kwargs):
        # What an ugly hack to avoid the 'Cannot combine queries on two different base models.' error
        # otherweise return self.get_children().specific().live() would be the right thing
        return Container.objects.filter(id__in=[c.id for c in self.get_children()]).live()


class ContainerQuery(object):
    categories = DjangoFilterConnectionField(CategoryNode)
    containers = DjangoFilterConnectionField(ContainerNode)
    units = DjangoFilterConnectionField(UnitNode)

    def resolve_categories(self, *args, **kwargs):
        return Category.objects.filter(**kwargs).live()

    def resolve_containers(self, *args, **kwargs):
        return Container.objects.filter(**kwargs).live()

    def resolve_units(self, *args, **kwargs):
        return Unit.objects.filter(**kwargs).live()

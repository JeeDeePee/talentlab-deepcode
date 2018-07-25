import graphene
from graphene import relay
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from focus.models import Competence, CompetenceEntry, Focus


class CompetenceNode(DjangoObjectType):
    class Meta:
        model = Competence
        filter_fields = ['title', 'slug', 'category__slug', 'category__title']
        interfaces = (relay.Node,)


class CompetenceEntryNode(DjangoObjectType):
    class Meta:
        model = CompetenceEntry
        interfaces = (relay.Node,)


class FocusNode(DjangoObjectType):
    pk = graphene.Int()

    class Meta:
        model = Focus
        filter_fields = ['user__username', 'active']
        interfaces = (relay.Node,)

    def resolve_pk(self, *args, **kwargs):
        return self.id


class FocusQuery(object):
    competences = DjangoFilterConnectionField(CompetenceNode)

    focus = relay.Node.Field(FocusNode)
    all_focus = DjangoFilterConnectionField(FocusNode)

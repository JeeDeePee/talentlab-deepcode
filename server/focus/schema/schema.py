import django_filters
import graphene
from graphene import relay
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from core.middleware import get_current_user
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
        interfaces = (relay.Node,)

    def resolve_pk(self, *args, **kwargs):
        return self.id


class UserFocusFilter(django_filters.FilterSet):
    class Meta:
        model = Focus
        fields = ['active']

    @property
    def qs(self):
        user = get_current_user()
        if not user:
            return Focus.objects.none()
        return super(UserFocusFilter, self).qs.filter(user=user)


class UserFocusQuery(object):
    user_focus = DjangoFilterConnectionField(FocusNode, filterset_class=UserFocusFilter)

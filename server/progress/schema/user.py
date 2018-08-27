import django_filters
import graphene
from graphene import relay
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from core.middleware import get_current_user
from user.models import User


class UserFilter(django_filters.FilterSet):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

    @property
    def qs(self):
        usr = get_current_user()
        return User.objects.filter(id=usr.id)


class UserNode(DjangoObjectType):
    class Meta:
        model = User
        filter_fields = ['username', 'email', 'first_name', 'last_name']
        interfaces = (relay.Node,)


class UserQuery(object):
    user_progress = graphene.Field(UserNode)

    all_users = DjangoFilterConnectionField(UserNode, filterset_class=UserFilter)

    def resolve_user_progress(self, *args, **kwargs):
        return get_current_user()

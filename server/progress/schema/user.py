from graphene import relay, ObjectType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from user.models import User


class UserNode(DjangoObjectType):
    class Meta:
        model = User
        filter_fields = ['username', 'email', 'first_name', 'last_name']
        interfaces = (relay.Node,)


class UserQuery(ObjectType):
    user_progress = relay.Node.Field(UserNode)
    all_users = DjangoFilterConnectionField(UserNode)

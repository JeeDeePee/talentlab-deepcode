import graphene
from graphene import relay
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from modules.schema import ModuleNode, UnitNode
from progress.models import UserUnit, UserModule
from user.models import User


class UserNode(DjangoObjectType):
    class Meta:
        model = User
        filter_fields = ['username', 'email', 'first_name', 'last_name']
        interfaces = (relay.Node, )


class UserUnitNode(DjangoObjectType):
    pk = graphene.Int()
    unit = DjangoFilterConnectionField(UnitNode)

    # synthetic attribute: started
    # has this unit been started by the user?
    # filter on this attribute

    class Meta:
        model = UserUnit
        filter_fields = []
        interfaces = (relay.Node, )

    def resolve_pk(self, info, *args):
        return self.id


class UserModuleNode(DjangoObjectType):
    pk = graphene.Int()
    user = UserNode
    module = ModuleNode
    user_units = DjangoFilterConnectionField(UserUnitNode)

    class Meta:
        model = UserModule
        filter_fields = ['user__username']
        interfaces = (relay.Node, )

    def resolve_pk(self, info, *args):
        return self.id


class ProgressQuery(object):
    user = relay.Node.Field(UserNode)
    all_users = DjangoFilterConnectionField(UserNode)

    user_module = relay.Node.Field(UserModuleNode)
    all_user_modules = DjangoFilterConnectionField(UserModuleNode)

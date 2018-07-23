import graphene
from graphene import relay, InputObjectType, Node
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from modules.models import Module
from modules.schema import ModuleNode, UnitNode
from progress.models import UserUnitProgress, UserModuleProgress
from user.models import User



class ProgressQuery(graphene.ObjectType):
    user = relay.Node.Field(UserNode)
    user_progress = relay.Node.Field(UserNode)

    all_users = DjangoFilterConnectionField(UserNode)

    module_progress = relay.Node.Field(ModuleProgressNode)
    all_modules_progress = DjangoFilterConnectionField(ModuleProgressNode)

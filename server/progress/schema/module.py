import graphene
from graphene import relay, Node
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from modules.models import Module
from modules.schema import ModuleNode
from progress.models import UserModuleProgress
from progress.schema.user import UserNode
from user.models import User


class ModuleProgressNode(DjangoObjectType):
    pk = graphene.Int()
    user = UserNode
    module = ModuleNode

    class Meta:
        model = UserModuleProgress
        filter_fields = ['user__username', 'module__slug']
        interfaces = (relay.Node,)

    def resolve_pk(self, info, *args):
        return self.id


class UserModuleNode(graphene.ObjectType):
    status = graphene.Boolean()
    module_progress = graphene.Field(ModuleProgressNode)
    module = graphene.Field(ModuleNode)

    class Meta:
        interfaces = (Node,)


class UserModuleConnection(graphene.Connection):
    class Meta:
        node = UserModuleNode


class UserModulesQuery(object):
    module_progress = relay.Node.Field(ModuleProgressNode)
    all_modules_progress = DjangoFilterConnectionField(ModuleProgressNode)

    user_modules = relay.ConnectionField(UserModuleConnection, username=graphene.String())

    def resolve_user_modules(self, info, **args):
        username = args['username']
        user_modules = []

        # TODO: definitely not performant, but shows what we can do directly in graphene
        # implement using a direct django join. Now doing definitely too many calls to db through the orm

        # master data
        user = User.objects.get(username=username)
        all_modules = list(Module.objects.all())

        # now calc module status
        for module in all_modules:
            module_progress = UserModuleProgress.objects.filter(user=user, module=module).first()
            user_modules.append(UserModuleNode(module_progress=module_progress,
                                               module=module,
                                               status=module_progress is not None))

        field = relay.ConnectionField.resolve_connection(UserModuleConnection, args, user_modules)
        return field

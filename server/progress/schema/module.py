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


class UserModulesQuery(graphene.ObjectType):
    module_progress = relay.Node.Field(ModuleProgressNode)
    all_modules_progress = DjangoFilterConnectionField(ModuleProgressNode)

    user_modules = relay.ConnectionField(UserModuleConnection, userid=graphene.String())

    def resolve_user_modules(self, info, **args):
        userid = args['userid']
        user_modules = []

        # TODO: definitely not performant, but shows what we can do directly in graphene
        # implement using a direct django join. Now doing definitely too many calls to db through the orm

        # master data
        user = User.objects.get(username=userid)
        all_modules = Module.objects.all()

        # now calc module status
        for module in all_modules:
            user_module = UserModuleProgress.objects.filter(user=user, module=module).first()
            user_modules.append(UserModuleNode(module_progress=user_module,
                                               module=module,
                                               status=user_module is not None))

        field = relay.ConnectionField.resolve_connection(UserModuleConnection, args, user_modules)
        return field

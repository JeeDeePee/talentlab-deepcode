import graphene
from graphene import relay, Node
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from core.graphql_filter import graphql_user_filter
from core.middleware import get_current_user
from modules.models import Module
from modules.schema import ModuleNode
from progress.models import UserModuleProgress
from progress.schema.user import UserNode


class UserModuleProgressNode(DjangoObjectType):
    user = UserNode
    module = ModuleNode

    class Meta:
        model = UserModuleProgress
        filter_fields = ['module__slug']
        interfaces = (relay.Node,)


class UserModuleNode(graphene.ObjectType):
    status = graphene.Boolean()
    module_progress = graphene.Field(UserModuleProgressNode)
    module = graphene.Field(ModuleNode)

    class Meta:
        interfaces = (Node,)


class UserModuleConnection(graphene.Connection):
    class Meta:
        node = UserModuleNode


class UserModulesQuery(object):
    module_progress = relay.Node.Field(UserModuleProgressNode)
    all_modules_progress = DjangoFilterConnectionField(UserModuleProgressNode)

    user_modules = relay.ConnectionField(UserModuleConnection)

    def resolve_all_modules_progress(self, info, **args):
        # TODO: Does not filter
        user = get_current_user()
        if user.is_authenticated:
            return UserModuleProgress.objects.filter(module__slug=args.get('module__slug'), user=user)

    def resolve_user_modules(self, info, **args):
        # TODO: definitely not performant, but shows what we can do directly in graphene
        # implement using a direct django join. Now doing definitely too many calls to db through the orm

        # master data
        user = get_current_user()
        all_modules = list(Module.objects.all())

        user_modules = []
        if user.is_authenticated:
            # now calc module status
            for module in all_modules:
                module_progress = UserModuleProgress.objects.filter(user=user, module=module).first()
                user_modules.append(UserModuleNode(module_progress=module_progress,
                                                   module=module,
                                                   status=module_progress is not None))

        field = relay.ConnectionField.resolve_connection(UserModuleConnection, args, user_modules)
        return field

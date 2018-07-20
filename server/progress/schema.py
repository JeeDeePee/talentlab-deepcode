import graphene
from graphene import relay, InputObjectType, Node
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from modules.models import Module
from modules.schema import ModuleNode, UnitNode
from progress.models import UserUnit, UserModule
from user.models import User


class UserNode(DjangoObjectType):
    class Meta:
        model = User
        filter_fields = ['username', 'email', 'first_name', 'last_name']
        interfaces = (relay.Node,)


class UnitProgressNode(DjangoObjectType):
    pk = graphene.Int()
    unit = DjangoFilterConnectionField(UnitNode)

    # synthetic attribute: started
    # has this unit been started by the user?
    # filter on this attribute

    class Meta:
        model = UserUnit
        filter_fields = []
        interfaces = (relay.Node,)

    def resolve_pk(self, info, *args):
        return self.id


# this node represents all units within a module along with a parameter
# informing whether the unit has been started or not
#
class ModuleUnitsNode(DjangoObjectType):
    pk = graphene.Int()
    # unit = DjangoFilterConnectionField(UnitNode)
    module_units = DjangoFilterConnectionField(UnitNode)

    # synthetic attribute: started
    # has this unit been started by the user?
    # filter on this attribute

    class Meta:
        model = UserUnit
        filter_fields = []
        interfaces = (relay.Node,)

    def resolve_pk(self, info, *args):
        return self.id

    def resolve_module_units(self, info, *args):
        return None


class ModuleProgressNode(DjangoObjectType):
    pk = graphene.Int()
    user = UserNode
    module = ModuleNode
    unit_progress = DjangoFilterConnectionField(UnitProgressNode)
    module_units = DjangoFilterConnectionField(ModuleUnitsNode)

    class Meta:
        model = UserModule
        filter_fields = ['user__username', 'module__slug']
        interfaces = (relay.Node,)

    def resolve_pk(self, info, *args):
        return self.id


class StartModuleProgress(graphene.Mutation):
    class Arguments:
        user_id = graphene.String()
        module_slug = graphene.String()

    created = graphene.Boolean()
    module_slug = graphene.String()

    def mutate(self, info, user_id, module_slug):
        user = User.objects.get(username=user_id)
        module = Module.objects.get(slug=module_slug)

        try:
            module, created = UserModule.objects.get_or_create(user=user, module=module)

            print('creating a user module {} for user {}'.format(module_slug, user_id))
            return StartModuleProgress(created=True, module_slug=module_slug)

        except Exception as ex:
            return StartModuleProgress(created=False, module_slug=module_slug)


class DeleteModuleProgress(graphene.Mutation):
    class Arguments:
        user_id = graphene.String()
        module_slug = graphene.String()

    deleted = graphene.Boolean()
    module_slug = graphene.String()

    def mutate(self, info, user_id, module_slug):
        user = User.objects.get(username=user_id)
        module = Module.objects.get(slug=module_slug)

        found_user_modules = UserModule.objects.filter(user=user, module=module)
        try:
            found_user_modules.delete()

            print('deleting a user module {} for user {}'.format(module_slug, user_id))
            return DeleteModuleProgress(deleted=True, module_slug=module_slug)

        except Exception as ex:
            return DeleteModuleProgress(deleted=False, module_slug=module_slug)


class InprogressModuleNode(graphene.ObjectType):
    status = graphene.Boolean()
    module = graphene.Field(ModuleNode)

    class Meta:
        interfaces = (Node, )


class InprogressConnection(graphene.Connection):
    class Meta:
        node = InprogressModuleNode


class InprogressQuery(graphene.ObjectType):
    inprogress = relay.ConnectionField(InprogressConnection, userid=graphene.String())

    def resolve_inprogress(self, info, **args):
        userid = args['userid']
        inprogress_modules = []

        # TODO: definitely not performant, but shows what we can do directly in graphene
        # implement using a direct django join. Now doing definitely too many calls to db through the orm

        all_modules = Module.objects.all()
        user = User.objects.get(username=userid)
        for module in all_modules:
            user_module = UserModule.objects.filter(user=user, module=module).first()
            inprogress_modules.append(InprogressModuleNode(module=module, status=user_module is not None))

        field = relay.ConnectionField.resolve_connection(InprogressConnection, args, inprogress_modules)
        return field


class ProgressMutations(graphene.ObjectType):
    start_module_progress = StartModuleProgress.Field()
    delete_module_progress = DeleteModuleProgress.Field()


class ProgressQuery(graphene.ObjectType):
    user = relay.Node.Field(UserNode)
    user_progress = relay.Node.Field(UserNode)

    all_users = DjangoFilterConnectionField(UserNode)

    module_progress = relay.Node.Field(ModuleProgressNode)
    all_modules_progress = DjangoFilterConnectionField(ModuleProgressNode)

    # module = relay.Node.Field(FancyModuleNode)
    # all_fancy = DjangoFilterConnectionField(FancyModuleNode)

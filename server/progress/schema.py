import graphene
from graphene import relay, InputObjectType
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


class UnitProgressNode(DjangoObjectType):
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
        interfaces = (relay.Node, )

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
        interfaces = (relay.Node, )

    def resolve_pk(self, info, *args):
        return self.id


class StartModuleProgress(graphene.Mutation):
    class Arguments:
        user_id = graphene.String()
        module_id = graphene.String()

    ok = graphene.Boolean()
    module_id = graphene.String()

    def mutate(self, info, module_id):
        print('creating a user module {}'.format(module_id))
        return StartModuleProgress(ok=True, module_id=module_id)


class ProgressMutations(graphene.ObjectType):
    create_user_module = StartModuleProgress.Field()


class ProgressQuery(object):
    user = relay.Node.Field(UserNode)
    user_progress = relay.Node.Field(UserNode)

    all_users = DjangoFilterConnectionField(UserNode)

    module_progress = relay.Node.Field(ModuleProgressNode)
    all_modules_progress = DjangoFilterConnectionField(ModuleProgressNode)

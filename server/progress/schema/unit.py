import graphene
from graphene import relay, Node
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from modules.schema import UnitNode
from progress.models import UserUnitProgress
from progress.schema.module import ModuleProgressNode


class UnitProgressNode(DjangoObjectType):
    pk = graphene.Int()
    user_module = ModuleProgressNode
    unit = UnitNode

    class Meta:
        model = UserUnitProgress
        filter_fields = ['user_module__user__username', 'user_module__module__slug']
        interfaces = (relay.Node,)

    def resolve_pk(self, info, *args):
        return self.id


class UserUnitNode(graphene.ObjectType):
    status = graphene.Boolean()
    unit = graphene.Field(UnitNode)

    class Meta:
        interfaces = (Node,)


class UserUnitConnection(graphene.Connection):
    class Meta:
        node = UserUnitNode


class UserUnitsQuery(graphene.ObjectType):
    unit_progress = relay.Node.Field(UnitProgressNode)
    all_unit_progress = DjangoFilterConnectionField(UnitProgressNode)

    # user_module_units = relay.ConnectionField(UserUnitConnection, userid=graphene.String())

    # module_progress = relay.Node.Field(ModuleProgressNode)
    # all_modules_progress = DjangoFilterConnectionField(ModuleProgressNode)
    # user_modules = relay.ConnectionField(UserUnitConnection, userid=graphene.String())

    # def resolve_user_module_units(self, info, **args):
    #     userid = args['userid']
    #     user_modules = []
    #
    #     # TODO: definitely not performant, but shows what we can do directly in graphene
    #     # implement using a direct django join. Now doing definitely too many calls to db through the orm
    #
    #     all_modules = Module.objects.all()
    #     user = User.objects.get(username=userid)
    #     for module in all_modules:
    #         user_module = UserUnitProgress.objects.filter(user=user, module=module).first()
    #         user_modules.append(UserUnitNode(module=module, status=user_module is not None))
    #
    #     field = relay.ConnectionField.resolve_connection(UserUnitConnection, args, user_modules)
    #     return field
    #
    #

import graphene
from graphene import relay, Node
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from modules.models import Unit, Module
from modules.schema import UnitNode
from progress.models import UserUnitProgress, UserModuleProgress
from progress.schema.module import ModuleProgressNode
from user.models import User


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

    user_module_units = relay.ConnectionField(UserUnitConnection,
                                              userid=graphene.String(),
                                              module_slug=graphene.String())

    def resolve_user_module_units(self, info, **args):
        userid = args['userid']
        module_slug = args['module_slug']

        # master data
        user = User.objects.get(username=userid)
        module = Module.objects.get(slug=module_slug)

        # progress data
        user_module = UserModuleProgress.objects.get(user=user, module=module)

        # all module units
        module_units = Unit.objects.filter(id__in=module.get_child_ids()).live()

        user_module_units = []
        for module_unit in module_units:
            user_unit_progress = UserUnitProgress.objects.filter(user_module=user_module, unit=module_unit).first()
            user_module_units.append(UserUnitNode(unit=module_unit, status=user_unit_progress is not None))

        field = relay.ConnectionField.resolve_connection(UserUnitConnection, args, user_module_units)
        return field

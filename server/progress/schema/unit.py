import graphene
from graphene import relay, Node
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from core.middleware import get_current_user
from modules.models import Unit, Module
from modules.schema import UnitNode
from progress.models import UserUnitProgress, UserModuleProgress
from progress.schema.module import UserModuleProgressNode


class UserUnitProgressNode(DjangoObjectType):
    module_progress = UserModuleProgressNode
    unit = UnitNode

    class Meta:
        model = UserUnitProgress
        filter_fields = ['module_progress__module__slug']
        interfaces = (relay.Node,)


class UserUnitNode(graphene.ObjectType):
    status = graphene.Boolean()
    unit = graphene.Field(UnitNode)

    class Meta:
        interfaces = (Node,)


class UserUnitConnection(graphene.Connection):
    class Meta:
        node = UserUnitNode


class UserUnitsQuery(object):
    unit_progress = relay.Node.Field(UserUnitProgressNode)
    all_unit_progress = DjangoFilterConnectionField(UserUnitProgressNode)

    user_module_units = relay.ConnectionField(UserUnitConnection, module_slug=graphene.String())

    def resolve_user_module_units(self, info, **args):
        module_slug = args['module_slug']

        # master data
        user = get_current_user()
        module = Module.objects.get(slug=module_slug)

        # progress data
        #
        # TODO: change back after fix in test data generation
        # module_progress = UserModuleProgress.objects.get(user=user, module=module)
        #
        module_progress = UserModuleProgress.objects.filter(user=user, module=module).first()

        # all module units
        module_units = Unit.objects.filter(id__in=module.get_child_ids()).live()

        user_module_units = []
        for module_unit in module_units:
            user_unit_progress = UserUnitProgress.objects.filter(module_progress=module_progress, unit=module_unit).first()
            user_module_units.append(UserUnitNode(unit=module_unit, status=user_unit_progress is not None))

        field = relay.ConnectionField.resolve_connection(UserUnitConnection, args, user_module_units)
        return field

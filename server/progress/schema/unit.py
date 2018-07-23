import graphene
from graphene import relay
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from modules.schema import UnitNode
from progress.models import UserUnitProgress


class UnitProgressNode(DjangoObjectType):
    pk = graphene.Int()
    unit = DjangoFilterConnectionField(UnitNode)

    # synthetic attribute: started
    # has this unit been started by the user?
    # filter on this attribute

    class Meta:
        model = UserUnitProgress
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
        model = UserUnitProgress
        filter_fields = []
        interfaces = (relay.Node,)

    def resolve_pk(self, info, *args):
        return self.id

    def resolve_module_units(self, info, *args):
        return None


# class UnitProgressQuery(graphene.ObjectType):
#     module_progress = relay.Node.Field(ModuleProgressNode)
#     all_modules_progress = DjangoFilterConnectionField(ModuleProgressNode)

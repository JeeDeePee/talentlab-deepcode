import graphene
from django.conf import settings
from graphene import relay
from graphene_django.debug import DjangoDebug

from focus.schema.mutations import FocusMutation
from focus.schema.schema import UserFocusQuery
from modules.schema import ModulesQuery
from progress.schema.goal import UserGoalQuery
from progress.schema.goal_mutations import UserGoalMutations
from progress.schema.module import UserModulesQuery
from progress.schema.module_mutations import ModuleProgressMutations
from progress.schema.unit import UserUnitsQuery
from progress.schema.unit_mutations import UnitProgressMutations
from progress.schema.user import UserQuery


class Query(UserGoalQuery, UserFocusQuery, UserUnitsQuery, UserModulesQuery, ModulesQuery, UserQuery, graphene.ObjectType):
    node = relay.Node.Field()

    if settings.DEBUG:
        debug = graphene.Field(DjangoDebug, name='__debug')


class Mutation(UserGoalMutations, FocusMutation, UnitProgressMutations, ModuleProgressMutations, graphene.ObjectType):

    if settings.DEBUG:
        debug = graphene.Field(DjangoDebug, name='__debug')


schema = graphene.Schema(query=Query, mutation=Mutation)

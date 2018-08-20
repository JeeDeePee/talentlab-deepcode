import graphene
from django.conf import settings
from graphene_django.debug import DjangoDebug

from focus.schema.mutations import FocusMutation
from focus.schema.schema import UserFocusQuery
from modules.schema import ModulesQuery
from progress.schema.goal import UserGoalQuery
from progress.schema.module import UserModulesQuery
from progress.schema.module_mutations import ModuleProgressMutations
from progress.schema.unit import UserUnitsQuery
from progress.schema.unit_mutations import UnitProgressMutations
from progress.schema.user import UserQuery


class Query(UserGoalQuery, UserFocusQuery, UserUnitsQuery, UserModulesQuery, ModulesQuery, UserQuery, graphene.ObjectType):
    # This class will inherit from multiple Queries

    if settings.DEBUG:
        debug = graphene.Field(DjangoDebug, name='__debug')


class Mutation(FocusMutation, UnitProgressMutations, ModuleProgressMutations, graphene.ObjectType):
    # This class will inherit from multiple Queries

    if settings.DEBUG:
        debug = graphene.Field(DjangoDebug, name='__debug')


schema = graphene.Schema(query=Query, mutation=Mutation)

import graphene
from django.conf import settings
from graphene_django.debug import DjangoDebug

from modules.schema import ModulesQuery
from progress.schema.module import UserModulesQuery
from progress.schema.module_mutations import ProgressMutations
from progress.schema.unit import UserUnitsQuery
from progress.schema.user import UserQuery


class Query(UserUnitsQuery, UserModulesQuery, ModulesQuery, UserQuery, graphene.ObjectType):
    # This class will inherit from multiple Queries

    if settings.DEBUG:
        debug = graphene.Field(DjangoDebug, name='__debug')


class Mutation(ProgressMutations, graphene.ObjectType):
    # This class will inherit from multiple Queries

    if settings.DEBUG:
        debug = graphene.Field(DjangoDebug, name='__debug')


schema = graphene.Schema(query=Query, mutation=Mutation)

import graphene
from django.conf import settings
from graphene_django.debug import DjangoDebug

from modules.schema import ModulesQuery
from progress.schema import ProgressQuery, ProgressMutations


class Query(ModulesQuery, ProgressQuery, graphene.ObjectType):
    # This class will inherit from multiple Queries

    if settings.DEBUG:
        debug = graphene.Field(DjangoDebug, name='__debug')


class Mutation(ProgressMutations, graphene.ObjectType):
    # This class will inherit from multiple Queries

    if settings.DEBUG:
        debug = graphene.Field(DjangoDebug, name='__debug')


schema = graphene.Schema(query=Query, mutation=Mutation)

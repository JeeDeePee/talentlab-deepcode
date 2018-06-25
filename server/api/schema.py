import graphene
from graphene_django.debug import DjangoDebug
from modules.schema import ModulesQuery
from django.conf import settings


class Query(ModulesQuery, graphene.ObjectType):
    # This class will inherit from multiple Queries

    if settings.DEBUG:
        debug = graphene.Field(DjangoDebug, name='__debug')


# class Mutation(graphene.ObjectType):
# This class will inherit from multiple Queries
#    pass


schema = graphene.Schema(query=Query)  # , mutation=Mutation

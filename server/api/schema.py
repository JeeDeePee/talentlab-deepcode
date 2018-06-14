import graphene

from containers.schema import ContainerQuery


class Query(ContainerQuery, graphene.ObjectType):
    # This class will inherit from multiple Queries
    pass


#class Mutation(graphene.ObjectType):
    # This class will inherit from multiple Queries
#    pass


schema = graphene.Schema(query=Query) # , mutation=Mutation

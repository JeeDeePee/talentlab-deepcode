import graphene
from graphene_django import DjangoObjectType
from containers.models import Container


class ContainerNode(DjangoObjectType):

    content = graphene.JSONString()

    class Meta:
        model = Container
        only_fields = ['id', 'title', 'intro']

    def resolve_content(self, *args, **kwargs):
        # @todo: use subtypes!
        return self.content.stream_data


class Query(graphene.ObjectType):
    containers = graphene.List(ContainerNode)

    @graphene.resolve_only_args
    def resolve_containers(self):
        return Container.objects.live()


schema = graphene.Schema(query=Query)

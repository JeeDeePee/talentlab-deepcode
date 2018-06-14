from graphene import relay
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
import graphene
from .models import Container


class ContainerNode(DjangoObjectType):
    content = graphene.JSONString()
    pk = graphene.Int()

    class Meta:
        model = Container
        exclude_fields = ['content']
        filter_fields = {
            'title': ['exact', 'icontains', 'in'],
            'intro': ['exact', 'icontains', 'in'],
        }

        interfaces = (relay.Node,)

    def resolve_content(self, *args, **kwargs):
        # @todo: use subtypes!
        return self.content.stream_data

    def resolve_pk(self, *args, **kwargs):
        # @todo: use subtypes!
        return self.id


class ContainerQuery(object):
    containers = DjangoFilterConnectionField(ContainerNode)

    def resolve_containers(self, *args, **kwargs):
        return Container.objects.filter(**kwargs).live()

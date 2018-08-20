import graphene
from graphene import relay
from graphene_django import DjangoObjectType

from progress.models import UserGoal


class UserGoalNode(DjangoObjectType):
    pk = graphene.Int()

    class Meta:
        model = UserGoal
        filter_fields = ['user__username', 'goal__module__slug']
        interfaces = (relay.Node,)

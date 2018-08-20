import graphene
from graphene import relay
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from progress.models import UserGoal


class UserGoalNode(DjangoObjectType):
    pk = graphene.Int()

    class Meta:
        model = UserGoal
        filter_fields = ['user__username', 'goal__module__slug']
        interfaces = (relay.Node,)

    def resolve_pk(self, *args, **kwargs):
        return self.id


class UserGoalQuery(object):
    user_goal = relay.Node.Field(UserGoalNode)
    all_user_goals = DjangoFilterConnectionField(UserGoalNode)

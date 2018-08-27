import graphene
from core.graphql_filter import graphql_user_filter
from graphene import relay
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from core.middleware import get_current_user
from progress.models import UserGoal


class UserGoalNode(DjangoObjectType):
    pk = graphene.Int()

    class Meta:
        model = UserGoal
        interfaces = (relay.Node,)

    def resolve_pk(self, *args, **kwargs):
        return self.id


filterset_class = graphql_user_filter(UserGoal, ['goal__module__slug'])


class UserGoalQuery(object):
    user_goal = relay.Node.Field(UserGoalNode, filterset_class=filterset_class)
    module_user_goal = graphene.Field(UserGoalNode, module_slug=graphene.String())

    all_user_goals = DjangoFilterConnectionField(UserGoalNode, filterset_class=filterset_class)

    def resolve_module_user_goal(self, info, **kwargs):
        user = get_current_user()
        module_slug = kwargs.get('module_slug')

        if module_slug is not None:
            return UserGoal.objects.get(goal__module__slug=module_slug, user=user)
        return []

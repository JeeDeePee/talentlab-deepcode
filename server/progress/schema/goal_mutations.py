import graphene

from core.middleware import get_current_user
from modules.models import Goal
from progress.models import UserGoal


class DefineUserGoal(graphene.Mutation):
    class Arguments:
        module_slug = graphene.String()
        goal_id = graphene.String()

    ok = graphene.Boolean()
    user_goal = graphene.Field(UserGoal)

    def mutate(self, module_slug, goal_id):
        current_user = get_current_user()
        user_goal = None
        try:
            user_goal = UserGoal.objects.get(goal__module__slug=module_slug, user=current_user)

            # we have the user goal, update it
            goal = Goal.objects.get(id=goal_id)
            user_goal.goal = goal
            user_goal.save()

        except Exception as ex:

            # we don't have the user goal, create a new one
            goal = Goal.objects.get(id=goal_id)
            user_goal = UserGoal(user=current_user, goal=goal)
            user_goal.save()

        return DefineUserGoal(user_goal=user_goal, ok=True)


class UserGoalMutations(object):
    define_user_goal = DefineUserGoal.Field()

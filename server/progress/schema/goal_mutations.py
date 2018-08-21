import graphene

from core.middleware import get_current_user
from modules.models import Goal
from progress.models import UserGoal
from progress.schema.goal import UserGoalNode


class DefineUserGoal(graphene.Mutation):
    CREATE = 'create'
    UPDATE = 'update'

    class Arguments:
        module_slug = graphene.String()
        goal_level = graphene.String()

    ok = graphene.Boolean()
    message = graphene.String()
    user_goal = graphene.Field(UserGoalNode)

    def mutate(self, info, module_slug, goal_level):
        current_user = get_current_user()
        try:
            user_goal = UserGoal.objects.filter(goal__module__slug=module_slug, user__username=current_user.username)
            found_goals = len(user_goal)
            if found_goals == 1:
                user_goal = list(user_goal)[0]

                # we have the user goal, update it
                goal = Goal.objects.get(module__slug=module_slug, level=goal_level)
                user_goal.goal = goal
                user_goal.save()

                return DefineUserGoal(ok=True, message=DefineUserGoal.UPDATE, user_goal=user_goal)

            elif found_goals == 0:

                # we don't have the user goal, create a new one
                goal = Goal.objects.get(module__slug=module_slug, level=goal_level)
                user_goal = UserGoal(user=current_user, goal=goal)
                user_goal.save()

                return DefineUserGoal(ok=True, message=DefineUserGoal.CREATE, user_goal=user_goal)

            else:
                return DefineUserGoal(ok=False, message='more than 1 UserGoal for module: {} and goal-level: {} found'.format(module_slug, goal_level))

        except Exception as ex:
            return DefineUserGoal(ok=False, message=ex)


class UserGoalMutations(object):
    define_user_goal = DefineUserGoal.Field()

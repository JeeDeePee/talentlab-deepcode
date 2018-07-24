import graphene

from modules.models import Unit, Module
from progress.models import UserUnitProgress, UserModuleProgress
from user.models import User


class StartUnitProgress(graphene.Mutation):
    class Arguments:
        username = graphene.String()
        unit_slug = graphene.String()
        module_slug = graphene.String()

    created = graphene.Boolean()
    unit_slug = graphene.String()
    failed = graphene.Boolean()
    exception = graphene.String()

    def mutate(self, info, username, unit_slug, module_slug):
        user = User.objects.get(username=username)
        module = Module.objects.get(slug=module_slug)
        unit = Unit.objects.get(slug=unit_slug)

        try:
            module_progress = UserModuleProgress.objects.get(user=user, module=module)
            unit, created = UserUnitProgress.objects.get_or_create(module_progress=module_progress, unit=unit)

            print('creating a user module {} for user {}'.format(unit_slug, username))
            return StartUnitProgress(created=True, unit_slug=unit_slug)

        except Exception as ex:
            return StartUnitProgress(created=False, unit_slug=unit_slug, failed=True, exception=ex)


class UnitProgressMutations(object):
    start_unit_progress = StartUnitProgress.Field()

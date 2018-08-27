import graphene

from core.middleware import get_current_user
from modules.models import Unit, Module
from progress.models import UserUnitProgress, UserModuleProgress


class StartUnitProgress(graphene.Mutation):
    class Arguments:
        unit_slug = graphene.String()
        module_slug = graphene.String()

    created = graphene.Boolean()
    unit_slug = graphene.String()
    failed = graphene.Boolean()
    exception = graphene.String()

    def mutate(self, info, unit_slug, module_slug):
        current_user = get_current_user()
        module = Module.objects.get(slug=module_slug)
        unit = Unit.objects.get(slug=unit_slug)

        try:
            module_progress = UserModuleProgress.objects.get(user=current_user, module=module)
            unit, created = UserUnitProgress.objects.get_or_create(module_progress=module_progress, unit=unit)

            return StartUnitProgress(created=True, unit_slug=unit_slug)

        except Exception as ex:
            return StartUnitProgress(created=False, unit_slug=unit_slug, failed=True, exception=ex)


class UnitProgressMutations(object):
    start_unit_progress = StartUnitProgress.Field()

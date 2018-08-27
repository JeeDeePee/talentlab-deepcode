import graphene

from core.middleware import get_current_user
from modules.models import Module
from progress.models import UserModuleProgress


class StartModuleProgress(graphene.Mutation):
    class Arguments:
        module_slug = graphene.String()

    created = graphene.Boolean()
    module_slug = graphene.String()
    failed = graphene.Boolean()
    exception = graphene.String()

    def mutate(self, info, module_slug):
        current_user = get_current_user()
        module = Module.objects.get(slug=module_slug)

        try:
            module, created = UserModuleProgress.objects.get_or_create(user=current_user, module=module)
            return StartModuleProgress(created=True, module_slug=module_slug)

        except Exception as ex:
            return StartModuleProgress(created=False, module_slug=module_slug, failed=True, exception=ex)


class DeleteModuleProgress(graphene.Mutation):
    class Arguments:
        module_slug = graphene.String()

    deleted = graphene.Boolean()
    module_slug = graphene.String()
    failed = graphene.Boolean()
    exception = graphene.String()

    def mutate(self, info, module_slug):
        current_user = get_current_user()
        module = Module.objects.get(slug=module_slug)

        found_module_progress = UserModuleProgress.objects.filter(user=current_user, module=module)
        try:
            found_module_progress.delete()
            return DeleteModuleProgress(deleted=True, module_slug=module_slug)

        except Exception as ex:
            return DeleteModuleProgress(deleted=False, module_slug=module_slug, failed=True, exception=ex)


class ModuleProgressMutations(object):
    start_module_progress = StartModuleProgress.Field()
    delete_module_progress = DeleteModuleProgress.Field()

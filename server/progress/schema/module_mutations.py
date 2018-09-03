import graphene
from django.shortcuts import get_object_or_404

from core.middleware import get_current_user
from modules.models import Module
from progress.models import UserModuleProgress
from progress.schema.module import UserModuleProgressNode


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


class DefineActionPlan(graphene.relay.ClientIDMutation):
    class Input:
        module_slug = graphene.String(required=True)
        # text params
        impact_text = graphene.String()
        measurement_text = graphene.String()
        measures_text = graphene.String()
        time_frame_text = graphene.String()
        resources_skills_text = graphene.String()
        commitment_support_text = graphene.String()

    user_module_progress = graphene.Field(UserModuleProgressNode)

    @classmethod
    def mutate_and_get_payload(cls, *args, **kwargs):
        user_module_progress = get_object_or_404(
            UserModuleProgress,
            user=get_current_user(),
            module__slug=kwargs.pop('module_slug')
        )

        for k, v in kwargs.items():
            setattr(user_module_progress, k, v)

        user_module_progress.save()
        return cls(user_module_progress=user_module_progress)


class ModuleProgressMutations(object):
    start_module_progress = StartModuleProgress.Field()
    delete_module_progress = DeleteModuleProgress.Field()
    define_action_plan = DefineActionPlan.Field()

import graphene

from modules.models import Module
from progress.models import UserModuleProgress
from user.models import User


class StartModuleProgress(graphene.Mutation):
    class Arguments:
        username = graphene.String()
        module_slug = graphene.String()

    created = graphene.Boolean()
    module_slug = graphene.String()

    def mutate(self, info, username, module_slug):
        user = User.objects.get(username=username)
        module = Module.objects.get(slug=module_slug)

        try:
            module, created = UserModuleProgress.objects.get_or_create(user=user, module=module)

            print('creating a user module {} for user {}'.format(module_slug, username))
            return StartModuleProgress(created=True, module_slug=module_slug)

        except Exception as ex:
            return StartModuleProgress(created=False, module_slug=module_slug)


class DeleteModuleProgress(graphene.Mutation):
    class Arguments:
        username = graphene.String()
        module_slug = graphene.String()

    deleted = graphene.Boolean()
    module_slug = graphene.String()

    def mutate(self, info, username, module_slug):
        user = User.objects.get(username=username)
        module = Module.objects.get(slug=module_slug)

        found_user_modules = UserModuleProgress.objects.filter(user=user, module=module)
        try:
            found_user_modules.delete()

            print('deleting a user module {} for user {}'.format(module_slug, username))
            return DeleteModuleProgress(deleted=True, module_slug=module_slug)

        except Exception as ex:
            return DeleteModuleProgress(deleted=False, module_slug=module_slug)


class ProgressMutations(graphene.ObjectType):
    start_module_progress = StartModuleProgress.Field()
    delete_module_progress = DeleteModuleProgress.Field()

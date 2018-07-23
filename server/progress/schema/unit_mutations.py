import graphene

from modules.models import Module
from progress.models import UserModuleProgress
from user.models import User


class StartUnitProgress(graphene.Mutation):
    class Arguments:
        username = graphene.String()
        unit_slug = graphene.String()

    created = graphene.Boolean()
    unit_slug = graphene.String()

    def mutate(self, info, username, module_slug):
        user = User.objects.get(username=username)
        module = Module.objects.get(slug=module_slug)

        try:
            module, created = UserModuleProgress.objects.get_or_create(user=user, module=module)

            print('creating a user module {} for user {}'.format(module_slug, username))
            return StartUnitProgress(created=True, module_slug=module_slug)

        except Exception as ex:
            return StartUnitProgress(created=False, module_slug=module_slug)


class UnitProgressMutations(graphene.ObjectType):
    start_unit_progress = StartUnitProgress.Field()


# class UnitProgressNode(DjangoObjectType):
#     pk = graphene.Int()
#     user_module = ModuleProgressNode
#     unit = UnitNode
#
#     class Meta:
#         model = UserUnitProgress
#         filter_fields = ['user_module__user__username', 'user_module__module__slug']
#         interfaces = (relay.Node,)
#
#     def resolve_pk(self, info, *args):
#         return self.id
#
#
# class UserUnitNode(graphene.ObjectType):
#     status = graphene.Boolean()
#     unit = graphene.Field(UnitNode)
#
#     class Meta:
#         interfaces = (Node,)
#
#
# class UserUnitConnection(graphene.Connection):
#     class Meta:
#         node = UserUnitNode
#
#
# class UserUnitsQuery(graphene.ObjectType):
#     unit_progress = relay.Node.Field(UnitProgressNode)
#     all_unit_progress = DjangoFilterConnectionField(UnitProgressNode)
#
#     user_module_units = relay.ConnectionField(UserUnitConnection,
#                                               username=graphene.String(),
#                                               module_slug=graphene.String())
#
#     def resolve_user_module_units(self, info, **args):
#         username = args['username']
#         module_slug = args['module_slug']
#
#         # master data
#         user = User.objects.get(username=username)
#         module = Module.objects.get(slug=module_slug)
#
#         # progress data
#         # TODO: change back after fix in test data generation
#         # user_module = UserModuleProgress.objects.get(user=user, module=module)
#         #
#         user_module = UserModuleProgress.objects.filter(user=user, module=module).first()
#
#         # all module units
#         module_units = Unit.objects.filter(id__in=module.get_child_ids()).live()
#
#         user_module_units = []
#         for module_unit in module_units:
#             user_unit_progress = UserUnitProgress.objects.filter(user_module=user_module, unit=module_unit).first()
#             user_module_units.append(UserUnitNode(unit=module_unit, status=user_unit_progress is not None))
#
#         field = relay.ConnectionField.resolve_connection(UserUnitConnection, args, user_module_units)
#         return field

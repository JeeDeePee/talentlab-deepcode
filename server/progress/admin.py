from django.contrib import admin

from progress.models import ActionPlan, Evaluation, Target, UserUnit, UserModule


@admin.register(UserModule)
class UserModuleAdmin(admin.ModelAdmin):
    list_display = ('user', 'module')


@admin.register(UserUnit)
class UserUnitAdmin(admin.ModelAdmin):
    list_display = ('user_module', 'unit')


# @admin.register(Target)
# class TargetAdmin(admin.ModelAdmin):
#     pass
#
#
# @admin.register(ActionPlan)
# class ActionPlanAdmin(admin.ModelAdmin):
#     pass
#
#
# @admin.register(Evaluation)
# class EvaluationAdmin(admin.ModelAdmin):
#     pass
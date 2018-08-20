from django.contrib import admin

from progress.models import UserUnitProgress, UserModuleProgress, UserGoal


@admin.register(UserModuleProgress)
class UserModuleProgressAdmin(admin.ModelAdmin):
    list_display = ('user', 'module')
    list_filter = ('user', 'module')


@admin.register(UserUnitProgress)
class UserUnitProgressAdmin(admin.ModelAdmin):
    list_display = ('module_progress', 'unit')
    list_filter = ('module_progress__user', 'module_progress__module')


@admin.register(UserGoal)
class UserGoalAdmin(admin.ModelAdmin):
    list_display = ('user', 'goal', 'completed', 'custom_text')
    list_filter = ('user', 'goal')

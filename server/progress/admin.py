from django.contrib import admin

from progress.models import UserUnitProgress, UserModuleProgress


@admin.register(UserModuleProgress)
class UserModuleProgressAdmin(admin.ModelAdmin):
    list_display = ('user', 'module')
    list_filter = ('user', 'module')


@admin.register(UserUnitProgress)
class UserUnitProgressAdmin(admin.ModelAdmin):
    list_display = ('user_module', 'unit')
    list_filter = ('user_module__user', 'user_module__module')

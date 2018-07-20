from django.contrib import admin

from progress.models import UserUnit, UserModule


@admin.register(UserModule)
class UserModuleAdmin(admin.ModelAdmin):
    list_display = ('user', 'module')


@admin.register(UserUnit)
class UserUnitAdmin(admin.ModelAdmin):
    list_display = ('user_module', 'unit')

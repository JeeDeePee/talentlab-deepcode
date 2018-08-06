from django.contrib import admin

from modules.models import Unit, Module, Category
from modules.models.goal import Goal


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')


@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'skill', 'teaser', 'description')


@admin.register(Goal)
class GoalAdmin(admin.ModelAdmin):
    list_display = ('module', 'level', 'text')
    list_filter = ('module', 'level')


@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'type', 'teaser')

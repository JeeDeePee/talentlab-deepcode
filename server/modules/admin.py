from django.contrib import admin

from core.wagtail_utils import wagtail_parent_filter
from modules.models import Unit, Module, Goal, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'icon_component')


@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'skill', 'teaser', 'description')
    list_filter = (wagtail_parent_filter(Category, Module),)


@admin.register(Goal)
class GoalAdmin(admin.ModelAdmin):
    list_display = ('id', 'module', 'level', 'text')
    list_filter = ('module', 'level')


@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'type', 'teaser')
    list_filter = ('type', wagtail_parent_filter(Module, Unit),)

from django.contrib import admin

from modules.models import Unit, Module, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')


@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'skill', 'teaser', 'description')


@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'type', 'teaser')

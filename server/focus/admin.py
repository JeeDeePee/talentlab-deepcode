from django.contrib import admin

from focus.models import Competence, CompetenceEntry, Focus


@admin.register(Competence)
class CompetenceAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'category')


@admin.register(CompetenceEntry)
class CompetenceEntryAdmin(admin.ModelAdmin):
    list_display = ('competence', 'current_level', 'next_evaluation', 'focus')
    list_filter = ('focus__user', 'focus__id', 'focus__active')


@admin.register(Focus)
class FocusAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'active')
    list_filter = ('user', 'active')

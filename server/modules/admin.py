# -*- coding: utf-8 -*-
#
# orbit7 gmbh
# http://orbit7.ch/
#
# Copyright (c) 2018 orbit7 gmbh. All rights reserved.
#
# Created on 25/06/18
# @author: Pawel Kowalski <pawel.kowalski@orbit7.ch>
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

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

from progress.models import ActionPlan, Evaluation, Target, UserUnit, UserModule, UserProgress


@admin.register(UserProgress)
class UserProgressAdmin(admin.ModelAdmin):
    list_display = ('user', )


@admin.register(UserModule)
class UserModuleAdmin(admin.ModelAdmin):
    list_display = ('user_progress', 'module')


@admin.register(UserUnit)
class UserUnitAdmin(admin.ModelAdmin):
    list_display = ('user_module', 'unit')


@admin.register(Target)
class TargetAdmin(admin.ModelAdmin):
    pass


@admin.register(ActionPlan)
class ActionPlanAdmin(admin.ModelAdmin):
    pass


@admin.register(Evaluation)
class EvaluationAdmin(admin.ModelAdmin):
    pass

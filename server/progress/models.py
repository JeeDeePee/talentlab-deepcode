# -*- coding: utf-8 -*-
#
# orbit7 gmbh
# http://orbit7.ch/
#
# Copyright (c) 2018 orbit7 gmbh. All rights reserved.
#
# Created on 25/06/18
# @author: Pawel Kowalski <pawel.kowalski@orbit7.ch>
from django.contrib.auth import get_user_model
from django.db import models
from django_extensions.db.models import TimeStampedModel


# User progress in modules


class UserProgress(TimeStampedModel):
    class Meta:
        verbose_name = 'Fortschritt'
        verbose_name_plural = 'A Fortschritte'

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    proposed_modules = models.ManyToManyField('modules.Module', blank=True)

    def __str__(self):
        return '{}'.format(self.user)


class UserModule(TimeStampedModel):
    class Meta:
        verbose_name = 'Lernmodul-Fortschritt'
        verbose_name_plural = 'B Lernmodul-Fortschritte'

    user_progress = models.ForeignKey('progress.UserProgress', null=True, on_delete=models.CASCADE)
    module = models.ForeignKey('modules.Module', null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return '{} - {}'.format(self.user_progress, self.module)


class UserUnit(TimeStampedModel):
    class Meta:
        verbose_name = 'Lernangebot-Fortschritt'
        verbose_name_plural = 'C Lernangebote-Fortschritte'

    user_module = models.ForeignKey('progress.UserModule', null=True, on_delete=models.CASCADE)
    unit = models.ForeignKey('modules.Unit', null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return '{} - {}'.format(self.user_module, self.unit)


# Individual targets


class Target(TimeStampedModel):
    class Meta:
        verbose_name = 'Ziel'
        verbose_name_plural = 'D Ziele'

    user_progress = models.ForeignKey('progress.UserProgress', null=True, on_delete=models.CASCADE)
    module = models.ForeignKey('progress.UserModule', null=True, on_delete=models.SET_NULL)


class Evaluation(TimeStampedModel):
    class Meta:
        verbose_name = 'Evaluation'
        verbose_name_plural = 'E Evaluationen'

    target = models.ForeignKey('progress.Target', blank=True, null=True, on_delete=models.CASCADE)

    max = models.PositiveIntegerField('Max Value', default=10)
    current_value = models.PositiveIntegerField('Current Value', default=0)


class ActionPlan(TimeStampedModel):
    class Meta:
        verbose_name = 'Action Plan'
        verbose_name_plural = 'F Action Pläne'

    target = models.ForeignKey('progress.Target', blank=True, null=True, on_delete=models.CASCADE)

    max = models.PositiveIntegerField('Max Value', default=10)
    current_value = models.PositiveIntegerField('Current Value', default=0)

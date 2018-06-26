# -*- coding: utf-8 -*-
#
# orbit7 gmbh
# http://orbit7.ch/
#
# Copyright (c) 2018 orbit7 gmbh. All rights reserved.
#
# Created on 26/06/18
# @author: Pawel Kowalski <pawel.kowalski@orbit7.ch>
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


admin.site.register(User, UserAdmin)

from django.db import models

from core.wagtail_utils import StrictHierarchyPage


class CoachingTopic(StrictHierarchyPage):
    pass


class Coach(StrictHierarchyPage):
    pass



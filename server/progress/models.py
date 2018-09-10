from django.db import models
from django_extensions.db.models import TimeStampedModel


# User progress in learning modules


class UserModuleProgress(TimeStampedModel):
    class Meta:
        verbose_name = 'UserModuleProgress'
        verbose_name_plural = 'UserModules'

    user = models.ForeignKey('user.User', null=True, on_delete=models.CASCADE)
    module = models.ForeignKey('modules.Module', null=True, on_delete=models.SET_NULL)

    # action plan: maybe refactor into a separate model later
    # steps:
    #    ReviseGoals
    #    Learnings
    #    ActionPlanBusinessGoal
    #        impactText
    #        measurementText
    #    ActionPlanMeasures
    #        measuresText
    #        timeFrameText
    #        resourcesSkillsText
    #        commitmentSupportText
    #    ActionPlanOverview

    # Learnings
    learnings_text = models.TextField(null=True, blank=True)

    # ActionPlan - BusinessGoal
    impact_text = models.TextField(null=True, blank=True)
    measurement_text = models.TextField(null=True, blank=True)

    # ActionPlan - Measures
    measures_text = models.TextField(null=True, blank=True)
    time_frame_text = models.TextField(null=True, blank=True)
    resources_skills_text = models.TextField(null=True, blank=True)
    commitment_support_text = models.TextField(null=True, blank=True)

    def __str__(self):
        return 'UserModuleProgress {} - {}'.format(self.user, self.module)


class UserUnitProgress(TimeStampedModel):
    class Meta:
        verbose_name = 'UserUnitProgress'
        verbose_name_plural = 'UserUnits'

    module_progress = models.ForeignKey('progress.UserModuleProgress', null=True, on_delete=models.CASCADE)
    unit = models.ForeignKey('modules.Unit', null=True, on_delete=models.SET_NULL)

    # learning: maybe refactor into a separate model later
    # learning = models.TextField(null=True, blank=True, default=None)

    def __str__(self):
        return 'UserUnitProgress {} - {}'.format(self.module_progress, self.unit)


class UserGoal(TimeStampedModel):
    class Meta:
        verbose_name = 'UserGoal'
        verbose_name_plural = 'UserGoals'

    user = models.ForeignKey('user.User', null=True, on_delete=models.CASCADE)
    goal = models.ForeignKey('modules.Goal', null=False, on_delete=models.CASCADE)

    completed = models.BooleanField(null=False, default=False)
    custom_text = models.TextField(null=True, blank=True, default=None)

    def __str__(self):
        return 'UserGoal {} - {}'.format(self.user, self.goal)


# class ActionPlan()

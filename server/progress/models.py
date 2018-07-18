from django.db import models
from django_extensions.db.models import TimeStampedModel


# User progress in learning modules


class UserModule(TimeStampedModel):
    class Meta:
        verbose_name = 'UserModule'
        verbose_name_plural = 'UserModules'

    user = models.ForeignKey('user.User', null=True, on_delete=models.CASCADE)
    module = models.ForeignKey('modules.Module', null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return '{} - {}'.format(self.user, self.module)


class UserUnit(TimeStampedModel):
    class Meta:
        verbose_name = 'UserUnit'
        verbose_name_plural = 'UserUnits'

    user_module = models.ForeignKey('progress.UserModule', null=True, on_delete=models.CASCADE)
    unit = models.ForeignKey('modules.Unit', null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return '{} - {}'.format(self.user_module, self.unit)

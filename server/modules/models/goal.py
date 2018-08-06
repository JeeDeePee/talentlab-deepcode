from django.db import models


class Goal(models.Model):
    class Meta:
        verbose_name = 'Ziel'
        verbose_name_plural = 'Ziele'

    module = models.ForeignKey('modules.Module', null=True, on_delete=models.SET_NULL)

    level = models.PositiveIntegerField(default=0, null=True, blank=True, help_text='Ziel-Level')
    text = models.TextField()

    def __str__(self):
        return 'Goal {} - {}'.format(self.level, self.module)

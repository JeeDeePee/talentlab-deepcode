from django.db import models


class Goal(models.Model):
    class Meta:
        verbose_name = 'Ziel'
        verbose_name_plural = 'Ziele'

    module = models.ForeignKey('modules.Module', null=True, on_delete=models.SET_NULL)

    level = models.PositiveIntegerField(default=0, null=True, blank=True, help_text='Ziel-Level')
    text = models.TextField()

    def __str__(self):
        module_shortcut = ''.join(c for c in str(self.module) if c.isupper())
        text_shortcut = self.text[:30] if self.text else ''

        return 'Goal {} - {} - {}'.format(self.level, module_shortcut, text_shortcut)

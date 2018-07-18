from django.db import models


# Wohin die reise
from django_extensions.db.models import TimeStampedModel, TitleSlugDescriptionModel

from modules.models import Category


class Competence(TitleSlugDescriptionModel):
    class Meta:
        verbose_name = 'Kompetenz'
        verbose_name_plural = 'Kompetenzen'

    # a competence belongs to a specific category
    category = models.ForeignKey(Category, blank=False, null=False, on_delete=models.CASCADE)

    def __str__(self):
        return '{} - {}'.format(self.title, self.category)


class CompetenceEntry(TimeStampedModel):
    class Meta:
        verbose_name = 'Kompetenzeintrag'
        verbose_name_plural = 'Kompetenzeinträge'

    # several competence entries are grouped in current fokus
    focus = models.ForeignKey('focus.Focus', blank=False, null=False, on_delete=models.CASCADE)

    competence = models.ForeignKey(Competence, blank=False, null=False, on_delete=models.CASCADE)
    current_level = models.PositiveIntegerField('Kompetenzlevel', default=0)
    next_evaluation = models.DateField('Nächste Bewertung', null=True, blank=True)

    def __str__(self):
        return '({}) - {} - {}'.format(self.competence, self.current_level, self.next_evaluation)


class Focus(models.Model):
    class Meta:
        verbose_name = 'Fokus'
        verbose_name_plural = 'Fokus'

    user = models.ForeignKey('user.User', null=True, on_delete=models.CASCADE)

    def __str__(self):
        return 'Fokus {}'.format(self.user)

    # based on the focus we can propose modules
    def proposed_modules(self):

        # something like a cosine similarity
        # where the focus and the competences covered by a module are the vectors
        return None

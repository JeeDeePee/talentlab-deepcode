from django.db import models


# Wohin die reise
from django_extensions.mongodb.models import TitleSlugDescriptionModel, TimeStampedModel

from modules.models import Category


class Competence(TitleSlugDescriptionModel):
    class Meta:
        verbose_name = 'Kompetenz'
        verbose_name_plural = 'Kompetenzen'

    category = models.ForeignKey(Category, blank=False, null=False, on_delete=models.CASCADE)


class Focus(models.Model):
    class Meta:
        verbose_name = 'Fokus'
        verbose_name_plural = 'Fokus'

    # user


class CompetenceEntry(TimeStampedModel):
    class Meta:
        verbose_name = 'Kompetenz Eintrag'
        verbose_name_plural = 'Kompetenz Einträge'

    competence = models.ForeignKey(Competence, blank=False, null=False, on_delete=models.CASCADE)
    # fokus where this belongs
    # datum
    # current level

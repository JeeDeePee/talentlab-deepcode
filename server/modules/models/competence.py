from django.db import models
from django_extensions.db.models import TitleSlugDescriptionModel

from modules.models import Category


class Competence(TitleSlugDescriptionModel):
    class Meta:
        verbose_name = 'Kompetenz'
        verbose_name_plural = 'Kompetenzen'

    # a competence belongs to a specific category
    category = models.ForeignKey(Category, blank=False, null=False, on_delete=models.CASCADE)

    def __str__(self):
        return 'Competence {}-{}'.format(self.title, self.category)

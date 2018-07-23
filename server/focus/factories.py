import factory

from focus.models import Competence, CompetenceEntry, Focus
from modules.factories import CategoryFactory


class CompetenceFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Competence

    category = factory.SubFactory(CategoryFactory)


class CompetenceEntryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = CompetenceEntry

    # # several competence entries are grouped in current fokus
    # focus = models.ForeignKey('focus.Focus', blank=False, null=False, on_delete=models.CASCADE)
    #
    # competence = models.ForeignKey(Competence, blank=False, null=False, on_delete=models.CASCADE)
    # current_level = models.PositiveIntegerField('Kompetenzlevel', default=0)
    # next_evaluation = models.DateField('Nächste Bewertung', null=True, blank=True)


class FocusFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Focus

    # user = models.ForeignKey('user.User', null=True, on_delete=models.CASCADE)

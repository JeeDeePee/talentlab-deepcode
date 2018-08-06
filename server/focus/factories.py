import factory
from factory import SubFactory
from factory.fuzzy import FuzzyInteger

from focus.models import Competence, CompetenceEntry, Focus
from modules.factories import CategoryFactory
from user.models import User


class FocusFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Focus

    user = factory.Iterator(User.objects.all())


class CompetenceEntryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = CompetenceEntry

    focus = SubFactory(FocusFactory)

    competence = factory.Iterator(Competence.objects.all())
    current_level = FuzzyInteger(0, 10)
    next_evaluation = factory.Faker('future_date', end_date="+30d", tzinfo=None)

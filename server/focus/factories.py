import factory

from focus.models import Competence
from modules.factories import CategoryFactory


class CompetenceFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Competence

    category = factory.SubFactory(CategoryFactory)

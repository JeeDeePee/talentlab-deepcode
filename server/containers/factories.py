import random

import wagtail_factories
import factory
from factory.fuzzy import FuzzyChoice
from faker import Faker

from containers.models import Category, Container, Unit

fake = Faker('de_DE')


def fake_title(x):
    return fake.sentence(nb_words=random.randint(3, 6)).replace('.', '')


class BasePageFactory(wagtail_factories.PageFactory):
    title = factory.LazyAttribute(fake_title)


class CategoryFactory(BasePageFactory):
    class Meta:
        model = Category


class ContainerFactory(BasePageFactory):
    teaser = factory.LazyAttribute(lambda x: fake.sentence(nb_words=random.randint(8, 12)))
    skill = factory.LazyAttribute(fake_title)
    description = factory.LazyAttribute(lambda x: fake.text(max_nb_chars=200))

    class Meta:
        model = Container


class UnitFactory(BasePageFactory):
    teaser = factory.LazyAttribute(lambda x: fake.sentence(nb_words=random.randint(8, 12)))
    count = factory.LazyAttribute(fake_title)
    duration = factory.LazyAttribute(fake_title)
    type = factory.LazyAttribute(lambda x: random.choice(['webinar', 'kurs', 'coaching']))

    class Meta:
        model = Unit

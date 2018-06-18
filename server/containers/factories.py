import random
import wagtail_factories
import factory
from factory import CREATE_STRATEGY

from containers.models import Category, Container, Unit, LinkBlock
from core.factories import BasePageFactory, fake_title, fake, DummyImageFactory


class CategoryFactory(BasePageFactory):
    icon = factory.SubFactory(DummyImageFactory)

    class Meta:
        model = Category


class LinkBlockFactory(wagtail_factories.StructBlockFactory):
    description = factory.LazyAttribute(fake_title)
    url = factory.LazyAttribute(lambda x: fake.uri())

    class Meta:
        model = LinkBlock


class ContainerFactory(BasePageFactory):
    hero_image = factory.SubFactory(DummyImageFactory)
    teaser = factory.LazyAttribute(lambda x: fake.sentence(nb_words=random.randint(8, 12)))
    skill = factory.LazyAttribute(fake_title)
    description = factory.LazyAttribute(lambda x: fake.text(max_nb_chars=400))

    video_id = random.choice([22439234, 33488192, 32001208, 21294655, 9479342, 24456787])
    video_description = factory.LazyAttribute(lambda x: fake.text(max_nb_chars=200))

    resources = wagtail_factories.StreamFieldFactory({
        'link': LinkBlockFactory
    })

    tools = wagtail_factories.StreamFieldFactory({
        'link': LinkBlockFactory
    })

    class Meta:
        model = Container

    @classmethod
    def create(cls, **kwargs):
        for i in range(0, random.randint(3, 6)):
            kwargs['tools__{}__link__b'.format(i)] = None
        for i in range(0, random.randint(3, 6)):
            kwargs['resources__{}__link__b'.format(i)] = None

        return cls._generate(CREATE_STRATEGY, kwargs)


class UnitFactory(BasePageFactory):
    teaser = factory.LazyAttribute(lambda x: fake.sentence(nb_words=random.randint(8, 12)))
    count = factory.LazyAttribute(fake_title)
    duration = factory.LazyAttribute(fake_title)
    type = factory.LazyAttribute(lambda x: random.choice(['webinar', 'kurs', 'coaching']))

    class Meta:
        model = Unit

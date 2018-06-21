import random
import wagtail_factories
import factory
from factory import CREATE_STRATEGY

from containers.blocks import LinkBlock, DocumentBlock
from containers.models import Category, Container, Unit
from core.factories import BasePageFactory, fake_title, fake, DummyImageFactory, DummyDocumentFactory


class CategoryFactory(BasePageFactory):
    icon = factory.SubFactory(DummyImageFactory)

    class Meta:
        model = Category


class LinkBlockFactory(wagtail_factories.StructBlockFactory):
    description = factory.LazyAttribute(fake_title)
    url = factory.LazyAttribute(lambda x: fake.uri())

    class Meta:
        model = LinkBlock


class DocumentBlockFactory(wagtail_factories.StructBlockFactory):
    description = factory.LazyAttribute(fake_title)
    document = factory.SubFactory(DummyDocumentFactory)

    class Meta:
        model = DocumentBlock


class ContainerFactory(BasePageFactory):
    hero_image = factory.SubFactory(DummyImageFactory)
    teaser = factory.LazyAttribute(lambda x: fake.sentence(nb_words=random.randint(8, 12)))
    skill = factory.LazyAttribute(fake_title)
    description = factory.LazyAttribute(lambda x: fake.text(max_nb_chars=200))

    video_id = random.choice([274620659, 275716804, 269374180, 273656672, 275692750, 267406224])
    video_description = factory.LazyAttribute(lambda x: fake.text(max_nb_chars=200))

    resources = wagtail_factories.StreamFieldFactory({
        'link': LinkBlockFactory,
        'document': DocumentBlockFactory,
    })

    tools = wagtail_factories.StreamFieldFactory({
        'link': LinkBlockFactory,
        'document': DocumentBlockFactory,
    })

    class Meta:
        model = Container

    @classmethod
    def create(cls, **kwargs):
        for i in range(0, random.randint(3, 7)):
            kwargs['tools__{}__{}__b'.format(i, random.choice(['link', 'document']))] = None

        for i in range(0, random.randint(3, 7)):
            kwargs['resources__{}__{}__b'.format(i, random.choice(['link', 'document']))] = None

        return cls._generate(CREATE_STRATEGY, kwargs)


class UnitFactory(BasePageFactory):
    teaser = factory.LazyAttribute(lambda x: fake.sentence(nb_words=random.randint(8, 12)))
    count = factory.LazyAttribute(fake_title)
    duration = factory.LazyAttribute(fake_title)
    type = factory.LazyAttribute(lambda x: random.choice(['webinar', 'kurs', 'coaching']))

    class Meta:
        model = Unit

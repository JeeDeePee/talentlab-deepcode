import random
import wagtail_factories
import factory
from factory import CREATE_STRATEGY

from modules.blocks import LinkBlock, DocumentBlock
from modules.models import Category, Module, Unit
from core.factories import BasePageFactory, fake_title, fake, DummyImageFactory, DummyDocumentFactory
from modules.models.goal import Goal


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


class ModuleFactory(BasePageFactory):
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
        model = Module

    @classmethod
    def stream_field_magic(cls, kwargs, stream_field_name):
        if stream_field_name in kwargs:
            for idx, resource in enumerate(kwargs[stream_field_name]):
                value = resource['value']
                for jdx, field in enumerate(value):
                    kwargs['{}__{}__{}__{}'.format(stream_field_name, idx, resource['type'], field)] = value[field]
            del kwargs[stream_field_name]
        else:
            for i in range(0, random.randint(3, 7)):
                kwargs['{}__{}__{}__b'.format(stream_field_name, i, random.choice(['link', 'document']))] = None

    @classmethod
    def create(cls, **kwargs):
        cls.stream_field_magic(kwargs, 'resources')
        cls.stream_field_magic(kwargs, 'tools')
        return cls._generate(CREATE_STRATEGY, kwargs)


class GoalFactory(BasePageFactory):
    level = factory.LazyAttribute(lambda x: fake.int())
    goal_text = factory.LazyAttribute(lambda x: fake.sentence(nb_words=random.randint(8, 12)))

    class Meta:
        model = Goal


class UnitFactory(BasePageFactory):
    teaser = factory.LazyAttribute(lambda x: fake.sentence(nb_words=random.randint(8, 12)))
    count = factory.LazyAttribute(lambda x: '{} {}'.format(random.randint(8, 12), fake.word().title()))
    duration = factory.LazyAttribute(lambda x: '{} {}'.format(random.randint(8, 12), fake.word().title()))
    type = factory.LazyAttribute(lambda x: random.choice(['webinar', 'kurs', 'coaching']))

    class Meta:
        model = Unit

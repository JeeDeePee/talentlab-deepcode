import random
import wagtail_factories
import factory
from factory import CREATE_STRATEGY, SubFactory

from modules.blocks import LinkBlock, DocumentBlock
from modules.models import Category, Module, Unit, Competence, Goal
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


class CompetenceFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Competence

    category = factory.SubFactory(CategoryFactory)


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


class GoalFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Goal

    module = SubFactory(ModuleFactory)

    level = factory.LazyAttribute(lambda x: fake.int())
    text = factory.LazyAttribute(lambda x: fake.sentence(nb_words=random.randint(8, 12)))


class UnitFactory(BasePageFactory):
    class Meta:
        model = Unit

    teaser = factory.LazyAttribute(lambda x: fake.sentence(nb_words=random.randint(8, 12)))
    description = factory.LazyAttribute(lambda x: fake.sentence(nb_words=random.randint(12, 16)))
    count = factory.LazyAttribute(lambda x: '{} {}'.format(random.randint(8, 12), fake.word().title()))
    duration = factory.LazyAttribute(lambda x: '{} {}'.format(random.randint(8, 12), fake.word().title()))
    price = factory.LazyAttribute(lambda x: '{} {}'.format('CHF ', random.randint(50, 200)))
    type = factory.LazyAttribute(lambda x: random.choice(['webinar', 'kurs', 'coaching', 'tinder', 'lernfilm', 'webex']))

    @factory.post_generation
    def competences(self, create, extracted, **kwargs):
        if not create:
            # Simple build, do nothing.
            return

        if extracted:
            # A list of groups were passed in, use them
            competences = list(Competence.objects.filter(title__in=extracted))
            for competence in competences:
                self.competences.add(competence)

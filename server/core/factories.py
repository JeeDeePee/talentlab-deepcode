import random

import os
import wagtail_factories
import factory
from django.conf import settings
from factory.django import ImageField, FileField
from faker import Faker
from wagtail.documents.models import get_document_model
from wagtail.images import get_image_model
from wagtail_factories.factories import CollectionMemberFactory

fake = Faker('de_DE')


def fake_title(x):
    return fake.sentence(nb_words=random.randint(2, 4)).replace('.', '')


class BasePageFactory(wagtail_factories.PageFactory):
    title = factory.LazyAttribute(fake_title)


class DummyDocumentFactory(factory.DjangoModelFactory):
    class Meta:
        model = get_document_model()

    title = factory.LazyAttribute(fake_title)
    file = FileField(
        from_path=os.path.join(settings.BASE_DIR, 'core', 'static', 'doc', 'dummy.pdf')
    )


class DummyImageFactory(factory.DjangoModelFactory):
    class Meta:
        model = get_image_model()

    title = factory.LazyAttribute(fake_title)
    file = ImageField(
        from_path=os.path.join(settings.BASE_DIR, 'core', 'static', 'img', 'dummy.jpg')
    )

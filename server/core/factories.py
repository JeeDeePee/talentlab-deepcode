import random

import os
import wagtail_factories
import factory
from django.conf import settings
from factory.django import ImageField
from faker import Faker
from wagtail.images import get_image_model
from wagtail_factories.factories import CollectionMemberFactory

fake = Faker('de_DE')


def fake_title(x):
    return fake.sentence(nb_words=random.randint(3, 6)).replace('.', '')


class BasePageFactory(wagtail_factories.PageFactory):
    title = factory.LazyAttribute(fake_title)


class DummyImageFactory(CollectionMemberFactory):
    class Meta:
        model = get_image_model()

    title = factory.LazyAttribute(fake_title)
    file = ImageField(
        from_path=os.path.join(settings.BASE_DIR, 'core', 'static', 'img', 'dummy.jpg')
    )

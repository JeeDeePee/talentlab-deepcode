import random

import factory

from core.factories import fake
from modules.models import Module, Unit, Goal
from progress.models import UserUnitProgress, UserModuleProgress, UserGoal
from user.models import User


class UserModuleProgressFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = UserModuleProgress

    user = factory.Iterator(User.objects.all())
    module = factory.Iterator(Module.objects.all())


class UserUnitProgressFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = UserUnitProgress

    module_progress = factory.Iterator(UserModuleProgress.objects.all())
    unit = factory.Iterator(Unit.objects.all())

    # TODO: how to select units based on used module? => By using factoryboy traits alter!


class UserGoalFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = UserGoal

    user = factory.Iterator(User.objects.all())
    goal = factory.Iterator(Goal.objects.all())

    completed = factory.LazyAttribute(lambda x: bool(random.getrandbits(1)))
    custom_text = factory.LazyAttribute(lambda x: None if random.randint(1, 10) < 8 else fake.text(max_nb_chars=200))

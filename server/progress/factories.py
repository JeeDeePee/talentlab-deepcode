import random

import factory
from factory import SubFactory

from core.factories import UserFactory, fake
from modules.models import Module, Unit, Goal
from progress.models import UserUnitProgress, UserModuleProgress, UserGoal
from user.models import User


class UserModuleProgressFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = UserModuleProgress

    # retrieve existing objects using factory.Iterator
    user = factory.Iterator(User.objects.all())
    module = factory.Iterator(Module.objects.all())

    # create new objects
    # user = factory.SubFactory(UserFactory)
    # module = factory.SubFactory(ModuleFactory)


class UserUnitProgressFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = UserUnitProgress

    # retrieve existing objects using factory.Iterator
    module_progress = factory.Iterator(UserModuleProgress.objects.all())
    unit = factory.Iterator(Unit.objects.all())

    # TODO: maersu how to select units based on used module?
    # somehow by using factory.SelfAttribute('...')

    # create new objects
    # module_progress = factory.SubFactory(UserModuleProgressFactory)
    # unit = factory.SubFactory(UnitFactory)


class UserGoalFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = UserGoal

    user = factory.Iterator(User.objects.all())
    goal = factory.Iterator(Goal.objects.all())

    completed = factory.LazyAttribute(lambda x: bool(random.getrandbits(1)))
    custom_text = factory.LazyAttribute(lambda x: None if random.randint(1, 10) < 8 else fake.text(max_nb_chars=200))

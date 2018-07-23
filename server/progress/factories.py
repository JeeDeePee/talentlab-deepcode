import factory

from modules.models import Module, Unit
from progress.models import UserUnitProgress, UserModuleProgress
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
    user_module = factory.Iterator(UserModuleProgress.objects.all())
    unit = factory.Iterator(Unit.objects.all())

    # TODO: maersu how to select units based on used module?

    # create new objects
    # user_module = factory.SubFactory(UserModuleProgressFactory)
    # unit = factory.SubFactory(UnitFactory)

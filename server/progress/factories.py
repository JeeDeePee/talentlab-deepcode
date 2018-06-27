import factory

from modules.models import Module, Unit
from progress.models import UserUnit, UserModule
from user.models import User


class UserModuleFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = UserModule

    # retrieve existing objects using factory.Iterator
    user = factory.Iterator(User.objects.all())
    module = factory.Iterator(Module.objects.all())

    # create new objects
    # user = factory.SubFactory(UserFactory)
    # module = factory.SubFactory(ModuleFactory)


class UserUnitFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = UserUnit

    # retrieve existing objects using factory.Iterator
    user_module = factory.Iterator(UserModule.objects.all())
    unit = factory.Iterator(Unit.objects.all())

    # create new objects
    # user_module = factory.SubFactory(UserModuleFactory)
    # unit = factory.SubFactory(UnitFactory)

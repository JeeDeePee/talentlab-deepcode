import random

import wagtail_factories
from django.core.management import BaseCommand
from wagtail.core.models import Page

from containers.factories import CategoryFactory, ContainerFactory, UnitFactory

class Command(BaseCommand):

    def handle(self, *args, **options):
        Page.objects.delete()

        site = wagtail_factories.SiteFactory.create(is_default_site=True)

        for i in range(0, 3):
            category = CategoryFactory.create(parent=site.root_page)

            for i in range(0, random.randint(5, 11)):
                container = ContainerFactory.create(parent=category)

                for i in range(0, random.randint(4, 7)):
                    UnitFactory.create(parent=container)

import random

import os
import wagtail_factories
from django.conf import settings
from django.core.management import BaseCommand
from django.db.models.signals import pre_init, pre_save, post_save, pre_delete, post_delete, post_init
from factory.django import mute_signals
from wagtail.core.models import Page
from wagtail.documents.models import Document
from wagtail.images.models import Image
import shutil
from containers.factories import CategoryFactory, ContainerFactory, UnitFactory


class Command(BaseCommand):

    def ensure_clean_dir(self, folder):
        path = os.path.join(settings.MEDIA_ROOT, folder)
        if os.path.exists(path):
            shutil.rmtree(path)
        if not os.path.exists(path):
            os.makedirs(path)

    def handle(self, *args, **options):

        with mute_signals(pre_delete, post_delete):
            Page.objects.all().delete()
            Image.objects.all().delete()
            Document.objects.all().delete()

            self.ensure_clean_dir('images')
            self.ensure_clean_dir('original_images')
            self.ensure_clean_dir('documents')

            site = wagtail_factories.SiteFactory.create(is_default_site=True)

            for i in range(0, 3):
                category = CategoryFactory.create(parent=site.root_page)

                for i in range(0, random.randint(5, 11)):
                    container = ContainerFactory.create(parent=category)

                    for i in range(0, random.randint(4, 7)):
                        UnitFactory.create(parent=container)

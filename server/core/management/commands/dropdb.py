import os
import shutil

from django.conf import settings
from django.core import management
from django.core.management import BaseCommand
from django.db import connection


class Command(BaseCommand):

    def ensure_clean_dir(self, folder):
        path = os.path.join(settings.MEDIA_ROOT, folder)
        if os.path.exists(path):
            shutil.rmtree(path)
        if not os.path.exists(path):
            os.makedirs(path)

    def handle(self, *args, **options):
        with connection.cursor() as cursor:
            cursor.execute("DROP SCHEMA IF EXISTS public CASCADE;")
            cursor.execute(
                "CREATE SCHEMA IF NOT EXISTS public AUTHORIZATION {};".format(settings.DATABASES['default']['USER']))
            cursor.execute("GRANT ALL ON SCHEMA public TO postgres;")
        management.call_command('migrate', verbosity=0, interactive=False)

        self.ensure_clean_dir('images')
        self.ensure_clean_dir('original_images')
        self.ensure_clean_dir('documents')

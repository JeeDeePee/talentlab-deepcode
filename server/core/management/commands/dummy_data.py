import os
import random
import shutil

import wagtail_factories
from django.conf import settings
from django.core import management
from django.core.management import BaseCommand
from django.db import connection
from factory.django import ImageField
from wagtail.core.models import Page

from core.factories import UserFactory
from focus.factories import CompetenceFactory
from modules.factories import CategoryFactory, ModuleFactory, UnitFactory
from progress.factories import UserModuleProgressFactory, UserUnitProgressFactory
from progress.models import UserModuleProgress

data = [
    {
        'title': 'Mastering Complexity',
        'competences': ['Vernetzes Denken', 'Agilität', 'Innovationsfähigkeit', 'Entscheidungsfähigkeit'],
        'modules': [
            {
                'title': 'Partnering for Success',
                'skill': 'Vernetztes Denken',
                'teaser': 'Erfolgreiche Führung von Partnerschaften',
                'description': 'Im Zuge der digitalen Disruption brechen angestammte Wertschöpfungslogiken auf.  Dabei gewinnt die Zusammenarbeit mit  externen Partnern bei der Leistungserstellung  an Bedeutung. In diesem Lernmodul werden die Grundlagen zur erfolgreichen Führung von Partnerschaften vermittelt.',
                'video_description': '<b>Tim Kellenberger</b><br>Unser Fach-Experte erklärt, warum die professionelle Führung von Partnerschaften heute von entscheidender Bedeutung ist.',
                'units': [
                    {
                        'title': 'Partnering Modelle',
                        'teaser': 'Unternehmensübergreifende Zusammenarbeit kann entlang von …',
                        'type': 'webinar',
                        'count': '8 Lektionen',
                        'duration': '4 Stunden'
                    },
                    {
                        'title': 'Supply Chain Design',
                        'teaser': 'Wertschöpfungsketten unternehmensübergreifend gestalten und … ',
                        'type': 'webinar',
                        'count': '5 Lektionen',
                        'duration': '3 Stunden'
                    },
                    {
                        'title': 'Erfolgreich verhandeln',
                        'teaser': 'Partnerschaften basieren auf guten Verträgen, welche die Rollen … ',
                        'type': 'kurs',
                        'count': '1 Veranstaltung',
                        'duration': '1 Tag'
                    },
                ]
            },
            {
                'title': 'Effizient kommunizieren',
                'skill': 'Verhandlungsfähigkeit / Kooperationsfähigkeit',
                'teaser': 'Gezieltes Training für Führungsalltag und Verhandlung',
            },
        ]},
    {
        'title': 'Growing as a Leader',
        'competences': ['Leadership', 'Management', 'Unternehmerisches Handeln'],
        'modules': [
            {
                'title': 'Leading through Disruption',
                'skill': 'Leadership',
                'teaser': 'Gezieltes Training für erfahrene Führungskräfte',
                'description': 'Unternehmen agieren getrieben durch die Digitalisierung in einem hyperdynamischen und stetig komplexeren Umfeld unter hohem Leistungs-, Anpassungs- und Innovationsdruck. Hinzu kommen neue Arbeitsformen und veränderte Ansprüche der Millenial-Mitarbeiter. Das Lernmodul «Leading through Disruption» trainiert erfahrene Führungskräfte.',
                'video_description': '<b>Samuel Ryser</b><br>Unser Fach-Experte erläutert die Heraus-forderungen von Leadership in Zeiten von disruptiven Veränderungen.',
                'units': [
                    {
                        'title': 'Führungsschulung für Kader',
                        'teaser': 'Meistern Sie die steigenden Ansprüche an Führungskräfte',
                        'type': 'kurs',
                        'count': '3 Veranstaltungen',
                        'duration': 'je 2 Tage'
                    },
                    {
                        'title': 'Führungszirkel',
                        'teaser': 'In einem organisationsübergreifenden Führungszirkel Führungsfragen in …',
                        'type': 'kurs',
                        'count': '3 Veranstaltungen',
                        'duration': 'je 4 Stunden'
                    },
                    {
                        'title': 'Coaching-Abo',
                        'teaser': 'Online & Offline Sessions',
                        'type': 'coaching',
                        'count': '8 Sessions',
                        'duration': 'je 45 Minuten'
                    },
                ]
            },
            {
                'title': 'First-time Leader',
                'skill': 'Leadership',
                'teaser': 'Grundlagen und Basis-Training für junge Führungskräfte',
            },
        ]},
    {
        'title': 'Mastering Relations',
        'competences': ['Kooperationsfähigkeit', 'Networking', 'Konfliktfähigkeit', 'Verhandlungsfähigkeit']
    }
]


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

        site = wagtail_factories.SiteFactory.create(is_default_site=True)
        Page.objects.filter(title='Root').delete()

        category_images = [
            ImageField(from_path=os.path.join(settings.BASE_DIR, 'core/static/img/dummy/category0.png')),
            ImageField(from_path=os.path.join(settings.BASE_DIR, 'core/static/img/dummy/category1.png')),
            ImageField(from_path=os.path.join(settings.BASE_DIR, 'core/static/img/dummy/category2.png')),
        ]
        # category_images = [
        #     ImageField(from_path=os.path.join(settings.BASE_DIR, 'core/static/img/Mastering-Complexity.svg'), width=60, height=60),
        #     ImageField(from_path=os.path.join(settings.BASE_DIR, 'core/static/img/Growing-as-a-Leader.svg'), width=60, height=60),
        #     ImageField(from_path=os.path.join(settings.BASE_DIR, 'core/static/img/Mastering-Relations.svg'), width=60, height=60),
        # ]

        module_images = [
            ImageField(from_path=os.path.join(settings.BASE_DIR, 'core/static/img/dummy/module_0.png')),
            ImageField(from_path=os.path.join(settings.BASE_DIR, 'core/static/img/dummy/module_1.png')),
            ImageField(from_path=os.path.join(settings.BASE_DIR, 'core/static/img/dummy/module_2.png')),
            ImageField(from_path=os.path.join(settings.BASE_DIR, 'core/static/img/dummy/module_3.png')),
        ]

        u = UserFactory(
            username='test',
            is_staff=True,
            is_superuser=True
        )

        for i in range(0, 4):
            UserFactory(username='user{}'.format(i))

        for idx, category_data in enumerate(data):
            category = CategoryFactory.create(
                parent=site.root_page,
                title=category_data['title'],
                icon__file=category_images[idx % len(category_images)]
            )

            competence_titles = category_data['competences']
            for competence_title in competence_titles:
                CompetenceFactory.create(
                    title=competence_title,
                    category=category
                ).save()

            modules_data = category_data.get('modules', [])

            for i in range(0, random.randint(4, 7)):

                module_data = modules_data[i] if len(modules_data) > i else {}
                module = ModuleFactory.create(
                    parent=category,
                    hero_image__file=module_images[i % len(module_images)],
                    **{k: v for (k, v) in module_data.items() if k != 'units'}
                )
                units_data = module_data.get('units', [])

                for j in range(0, random.randint(3, 5)):
                    unit_data = units_data[j] if len(units_data) > j else {}
                    UnitFactory.create(parent=module, **unit_data)

        # create user progress
        UserModuleProgressFactory.create_batch(size=20)
        all_module_progress = UserModuleProgress.objects.all()
        for module_progress in all_module_progress:
            UserUnitProgressFactory.create_batch(size=3, module_progress=module_progress)

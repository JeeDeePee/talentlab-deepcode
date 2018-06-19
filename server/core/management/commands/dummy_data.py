import random

import os
import wagtail_factories
from django.conf import settings
from django.core.management import BaseCommand
from wagtail.core.models import Page
from wagtail.documents.models import Document
from wagtail.images.models import Image
import shutil
from containers.factories import CategoryFactory, ContainerFactory, UnitFactory

data = [
    {
        'title': 'Mastering Complexity', 'containers': [
        {
            'title': 'Partnering for Success',
            'skill': 'Vernetztes Denken',
            'teaser': 'Erfolgreiche Führung von Partnerschaften',
            'description': 'Im Zuge der digitalen Disruption brechen angestammte Wertschöpfungslogiken auf.  Dabei gewinnt die Zusammenarbeit mit  externen Partnern bei der Leistungserstellung  an Bedeutung. In diesem Lernmodul werden die Grundlagen zur erfolgreichen Führung von Partnerschaften vermittelt.',
            'video_description': '<b>Tim Kellenberger</b>Unser Fach-Experte erklärt, warum die professionelle Führung von Partnerschaften heute von entscheidender Bedeutung ist.',
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
                    'type': 'webinar',
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
        'title': 'Growing as a Leader', 'containers': [
        {
            'title': 'Leading through Disruption',
            'skill': 'Leadership',
            'teaser': 'Gezieltes Training für erfahrene Führungskräfte',
        },
        {
            'title': 'First-time Leader',
            'skill': 'Leadership',
            'teaser': 'Grundlagen und Basis-Training für junge Führungskräfte',
        },
    ]},
    {
        'title': 'Mastering Relations'
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

        Page.objects.all().delete()
        Image.objects.all().delete()
        Document.objects.all().delete()

        self.ensure_clean_dir('images')
        self.ensure_clean_dir('original_images')
        self.ensure_clean_dir('documents')

        site = wagtail_factories.SiteFactory.create(is_default_site=True)

        for category_data in data:
            category = CategoryFactory.create(parent=site.root_page, title=category_data['title'])

            containers_data = category_data.get('containers', [])

            for i in range(0, random.randint(5, 11)):

                container_data = containers_data[i] if len(containers_data) > i else {}
                container = ContainerFactory.create(parent=category,
                                                    **{k: v for (k, v) in container_data.items() if k != 'units'})
                units_data = container_data.get('units', [])

                for i in range(0, random.randint(4, 7)):
                    unit_data = units_data[i] if len(units_data) > i else {}
                    UnitFactory.create(parent=container, **unit_data)

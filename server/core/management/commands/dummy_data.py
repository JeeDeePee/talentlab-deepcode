import os
import random
import shutil

import wagtail_factories
from django.conf import settings
from django.contrib.auth import get_user_model
from django.core import management
from django.core.management import BaseCommand
from django.db import connection
from factory.django import ImageField
from wagtail.core.models import Page

from core.factories import UserFactory, fake_title
from focus.factories import CompetenceEntryFactory, FocusFactory
from modules.factories import CategoryFactory, ModuleFactory, UnitFactory, GoalFactory, CompetenceFactory
from progress.factories import UserModuleProgressFactory, UserUnitProgressFactory, UserGoalFactory
from progress.models import UserModuleProgress

data = [
    {
        'title': 'Mastering Complexity',
        'icon': 'MasteringComplexity',
        'teaser': 'Gewinne Leichtigkeit im Umgang mit Veränderungen',
        'competences': [
            {
                'title': 'Vernetzes Denken',
                'description': 'Komplexität erkennen. Zusammenhänge und Abhängigkeiten erschliessen. Ein System aus übergeordneter Sicht betrachten und unterschiedliche Perspektiven einnehmen.'
            },
            {
                'title': 'Agilität',
                'description': 'Sich kontinuierlich auf neue Situationen einstellen und effektiv auf Veränderungen reagieren. Möglichkeiten und Chancen erkennen und nutzen. Veränderungen aktiv gestalten.'
            },
            {
                'title': 'Innovationsfähigkeit',
                'description': 'Über das Bekannte und herkömmliche Vorgehensweisen hinausgehen und ungewohnte, neue Sichtweisen eingehen, um Neues zu kreieren.'
            },
            {
                'title': 'Entscheidungsfähigkeit',
                'description': 'Situationsrelevante Informationen generieren und Handlungsoptionen ableiten. Umsichtig, verantwortungsvoll und nachhaltig entscheiden.'
            }
        ],
        'modules': [
            {
                'title': 'Digital Communication & Virtual Collaboration',
                'skill': 'Agilität',
                'teaser': 'Die richtigen Tools richtig einsetzen',
                'lead': 'Das Modul «Digital Communication & Virtual Collaboration» hilft Dir durch den Dschungel der digitalen Tools und befähigt Dich zum effizienten und effektiven Einsatz in Deinem Führungsalltag.',
                'description': 'Die Digitalisierung verändert die Art wie wir kommunizieren und die Art unserer Zusammenarbeit: Emails, Chats, Videokonferenzen … eine Vielzahl von tollen Tools erleichtern den Alltag. Doch: wer die Wahl hat, hat die Qual! Um Kommunikation und Koordination effizient zu gestalten, müssen die Tools bewusst eingesetzt werden. Zudem heisst digital kommunizieren auf Distanz kommunizieren und das schafft ganz eigene Herausforderung.',
                'video_description': '<b>Dr. Clea Bauch</b><br>Unsere Fach-Experten erläutert die Herausforderungen in Zusammenhang mit Führung und Kommunikation auf Distanz',
                'goals': [
                    {
                        'level': 1,
                        'text': 'Digitale Tools im Alltag professionell einsetzen, um Kommunikation und Zusammenarbeit zu verbessern.'
                    },
                    {
                        'level': 2,
                        'text': 'Die Herausforderungen von Kommunikation und Führung auf Distanz beherrschen.'
                    },
                    {
                        'level': 3,
                        'text': 'Die Organisation zur digitalen Kommunikation und virtuellen Zusammenarbeit befähigen.'
                    }
                ],
                'units': [
                    {
                        'title': 'Tools für digitale Kommunikation',
                        'teaser': 'Durchblick im Dschungel der Tools für digitale Kommunikation',
                        'lead': 'Verschaffe Dir Überblick! Gewinne Mitsprachekompetenz! Wähle passende Tools!',
                        'description': 'Wir stellen die wichtigsten Tools, ihre Vor- und Nachteile und sinnvolle Einsatzgebiete im unternehmerischen Alltag vor.<br>Verschaffe Dir Überblick!<br>Gewinne Mitsprachekompetenz!<br>Wähle passende Tools!',
                        'type': 'lernfilm',
                        'count': '1 Session',
                        'duration': '10 Minuten',
                        'price': 'inbegriffen',
                        'competences': ['Agilität', 'Kommunikation']
                    },
                    {
                        'title': 'Kommunikation auf Distanz',
                        'teaser': 'Die Fallstricke der Kommunikation auf Distanz umschiffen',
                        'lead': 'Vermeide Fehler! Kommuniziere mediengerecht! Stärke Deine Wirkung!',
                        'description': 'Wir zeigen Dir die klassischen Fallen und verraten die Tricks eines bewussten Umgangs mit Kommunikation auf Distanz.<br>Vermeide Fehler!<br>Kommuniziere mediengerecht!<br>Stärke Deine Wirkung!',
                        'type': 'lernfilm',
                        'count': 'x Sessions',
                        'duration': '45 Minuten',
                        'price': 'CHF 150',
                        'competences': ['Agilität', 'Kommunikation'],
                        'objectives': '<ul><li>Herausforderungen der digitalen Kommunikation kennen</li><li>Grundlagen der Kommunikation auf Distanz überblicken</li><li>Praxisorientierte Strategien zur Optimierung des eigenen Kommunikationsverhaltens erlernen</li></ul>',
                        'content': '<ul><li>Zweck und Funktionsweise von Kommunikation</li><li>Besonderheiten und Arten der Kommunikation auf Distanz</li><li>Grundlagen und Strategien der Kommunikation auf Distanz</li><li>Schriftliche Kommunikation</li><li>Audio-visuelle Kommunikation</li></ul>',
                        'teacher': '<p>Clea hat lange Jahre Erfahrung in der Energiebranche in verschiedenen operativen und strategischen Rollen. Heute ist sie in der Geschäftsleitung einer international tätigen Familienunternehmung, führt verschiedene Verwaltungsrats- und Stiftungsratsmandate und ist CEO ihrer eigenen Beratungsfirma. Sie hat im Verlaufe ihrer bisherigen Karriere stets international gearbeitet und hat deshalb weit reichende Erfahrung in Sachen Kommunikation und Führung auf Distanz.</p><p>Ihr Studium an der Universität Fribourg (CH) schloss sie mit dem Doktorat ab. Ihre Board-Zertifizierung hat sie am Insead (FR) im Rahmen des International Directors Program erlangt. Nebenberuflich unterrichtet Clea an verschiedenen Institutionen in der Schweiz und ist Learning Coach am Insead.</p>',
                        'requirements': '<ul><li>Bearbeitung aller Sessions</li><li>Quizzle zu den Tools für digitale Kommunikation</li><li>Quizzle zu den Tools für virtuelle Zusammenarbeit</li><li>Mini-Case-Study zur Kommunikation und Führung auf Distanz</li></ul>'
                    },
                    {
                        'title': 'Professionell kommunizieren',
                        'teaser': 'Unverzichtbare Kompetenz im Berufsalltag.',
                        'lead': 'Kommuniziere klar! Gewinne Sicherheit! Werde wirkungsvoll!',
                        'description': 'Wir bieten in Zusammenarbeit mit der BFH praxisorientierte Kommunikationstrainings an, speziell auf die Bedürfnisse zugeschnitten, für Dich 1-to-1 für Dein Team.<br>Kommuniziere klar!<br>Gewinne Sicherheit!<br>Werde wirkungsvoll!',
                        'type': 'kurs',
                        'count': '1 Session',
                        'duration': '2 Tage',
                        'price': 'CHF 800',
                        'competences': ['Kommunikation']
                    },
                    {
                        'title': 'Tools für virtuelle Teams',
                        'teaser': 'Durchblick im Dschungel der Tools für virtuelle Zusammenarbeit',
                        'lead': 'Verschaffe Dir Überblick! Gewinne Mitsprachekompetenz! Wähle passende Tools!',
                        'description': 'Wir stellen die wichtigsten Tools, ihre Vor- und Nachteile und sinnvolle Einsatzgebiete im unternehmerischen Alltag vor.<br>Verschaffe Dir Überblick!<br>Gewinne Mitsprachekompetenz!<br>Wähle passende Tools!',
                        'type': 'lernfilm',
                        'count': '1 Session',
                        'duration': '10 Minuten',
                        'price': 'inbegriffen',
                        'competences': ['Agilität', 'Kooperationsfähigkeit']
                    },
                    {
                        'title': 'Führen auf Distanz',
                        'teaser': 'Die Führung über verschiedene Standorte “remote“ verteilte Teams ist eine besondere Herausforderung.',
                        'lead': 'Vermeide Fehler! Stärke Deine Wirkung! Führe effektiv!',
                        'description': 'Wir zeigen Dir die klassischen Fallen und verraten die Tricks der Führung auf Distanz.<br>Vermeide Fehler!<br>Stärke Deine Wirkung!<br>Führe effektiv!',
                        'type': 'lernfilm',
                        'count': 'x Sessions',
                        'duration': '45 Minuten',
                        'price': 'CHF 150',
                        'competences': ['Agilität', 'Leadership']
                    },
                    {
                        'title': 'Coaching-Abonnement',
                        'teaser': 'Bespreche Deine Entwicklung mit einem Coach oder Mentor',
                        'lead': 'Finde Antworten! Werde wirkungsvoller! Entfalte Dein Potential!',
                        'description': 'talentlab bietet eine flexible Form von Coaching an – persönlich und digital!',
                        'type': 'interaktiv',
                        'count': '3 Sessions',
                        'duration': 'à 45 Minuten',
                        'price': 'CHF 700',
                        'competences': []
                    },
                    {
                        'title': 'Sparring mit Peers',
                        'teaser': 'Greife diskret und unkompliziert auf den Rat erfahrender Peers zu',
                        'lead': 'Profitiere von Erfahrung! Lass Dir helfen! Finde Lösungen!',
                        'description': 'Wir finden im Pool den besten Kontakt – diskret, schnell und unkompliziert.<br>Profitiere von Erfahrung!<br>Lass Dir helfen!<br>Finde Lösungen!',
                        'type': 'interaktiv',
                        'count': '1 Session',
                        'duration': '45 Minuten',
                        'price': 'inbegriffen',
                        'competences': []
                    },
                    {
                        'title': 'Un-Conference',
                        'teaser': 'Tausche Dich mit Peers aus!',
                        'lead': 'Erweitere Dein Wissen! Lerne von anderen! Zeige Deine Expertise!',
                        'description': 'Aktuelle Themen von talentlab moderiert, durch Teilnehmende gestaltet',
                        'type': 'interaktiv',
                        'count': '1 Session',
                        'duration': '45 Minuten',
                        'price': 'inbegriffen',
                        'competences': []
                    }
                ],
                'resources': [
                    {'type': 'document',
                     'value':
                         {
                             'description': 'K. Vollus: Welches Tool ist das Richtige?',
                             'url': 'https://ordnungsmentor.de/aufgabenverwaltung-tools/'
                         }
                     },
                    {'type': 'link',
                     'value':
                         {
                             'description': 'Trello: Task-Management',
                             'url': 'https://www.trello.com'
                         }
                     },
                    {'type': 'link',
                     'value':
                         {
                             'description': 'Meistertask: Task-Management',
                             'url': 'https://www.meistertask.com'
                         }
                     },
                    {'type': 'link',
                     'value':
                         {
                             'description': 'Slack: Team-Chat',
                             'url': 'https://www.slack.com'
                         }
                     }
                ],
                'tools': [
                    {'type': 'document',
                     'value':
                         {
                             'description': 'Info-Grafik: Tools für digitale Kommunkation',
                             'url': 'xxx'
                         }
                     },
                    {'type': 'document',
                     'value':
                         {
                             'description': 'Info-Grafik: Tools für virtuelle Zusammenarbeit',
                             'url': 'xxx'
                         }
                     }
                ]
            },
            {
                'title': 'Partnering for Success',
                'skill': 'Innovationsfähigkeit',
                'teaser': 'Erfolgreiche Führung von Partnerschaften',
                'description': 'Im Zuge der digitalen Disruption brechen angestammte Wertschöpfungslogiken auf.  Dabei gewinnt die Zusammenarbeit mit  externen Partnern bei der Leistungserstellung  an Bedeutung. In diesem Lernmodul werden die Grundlagen zur erfolgreichen Führung von Partnerschaften vermittelt.',
                'video_description': '<b>Tim Kellenberger</b><br>Unser Fach-Experte erklärt, warum die professionelle Führung von Partnerschaften heute von entscheidender Bedeutung ist.',
            },
            {
                'title': 'Decision Making & Agile',
                'skill': 'Entscheidungsfähigkeit',
                'teaser': 'Gute unternehmerische Entscheidungen in einem dynamischen Umfeld',
            },
            {
                'title': 'Project Management for IT Projects',
                'skill': 'Entscheidungsfähigkeit',
                'teaser': 'Training für erfahrene IT-Projektleiter',
            },
            {
                'title': 'Project Management for Business Projects',
                'skill': 'Innovationsfühigkeit',
                'teaser': 'Training für erfahrene Projektleiter in Business Development und Produktmanagement',
            },
            {
                'title': 'Building Successful Strategies',
                'skill': 'Innovationsfähigkeit',
                'teaser': 'Moderne Methoden der Strategiearbeit',
            }
        ]
    },
    {
        'title': 'Growing as a Leader',
        'icon': 'GrowingAsALeader',
        'teaser': 'Entfalte Dein Potenzial als Führungspersönlichkeit',
        'competences': [
            {
                'title': 'Leadership',
                'description': 'Vorbild sein, sinnvoll delegieren und Gestaltungsspielräume schaffen. Andere für die Sache gewinnen ihren Beitrag zum gemeinsamen Erfolg fördern und anerkennen.'
            },
            {
                'title': 'Management',
                'description': 'Prozesse planen und steuern. Aufgaben, Kompetenzen und Verantwortlichkeiten definieren und stufengerecht delegieren. Mitarbeitende gewinnen und einweisen. Ressourcen organisieren und Zielerreichung prüfen.'
            },
            {
                'title': 'Unternehmerisches Handeln',
                'description': 'Betriebswirtschaftliche Überlegungen integrieren. Strategische und ökonomische Potenziale erkennen und Spielräume nutzen. Unternehmerisch nachhaltig agieren.'
            }
        ],
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
                        'duration': 'je 2 Tage',
                        'competences': []
                    },
                    {
                        'title': 'Führungszirkel',
                        'teaser': 'In einem organisationsübergreifenden Führungszirkel Führungsfragen in …',
                        'type': 'interaktiv',
                        'count': '3 Veranstaltungen',
                        'duration': 'je 4 Stunden',
                        'competences': []
                    },
                    {
                        'title': 'Coaching-Abo',
                        'teaser': 'Online & Offline Sessions',
                        'type': 'interaktiv',
                        'count': '8 Sessions',
                        'duration': 'je 45 Minuten',
                        'competences': []
                    }
                ]
            },
            {
                'title': 'First-time Leader',
                'skill': 'Management',
                'teaser': 'Basis-Training für junge Führungskräfte'
            },
            {
                'title': 'Project Management Basics',
                'skill': 'Management',
                'teaser': 'Training für angehende Projektleiter'
            },
            {
                'title': '1st, 2nd & 3rd Career',
                'skill': 'Integrierte generationenübergreifende Führung',
                'teaser': 'Leadership'
            },
            {
                'title': 'Reorganisation &  Transformation',
                'skill': 'Management',
                'teaser': 'Erfolgreiche Umsetzung von Änderungsprojekten'
            },
            {
                'title': 'Agile Organisation',
                'skill': 'Management',
                'teaser': 'Zwischen agil dynamisch und dogmatisch holokratisch'
            }
        ]
    },
    {
        'title': 'Mastering Relations',
        'icon': 'MasteringRelations',
        'teaser': 'Lerne Beziehungen zielgerichtet zu gestalten',
        'competences': [
            {
                'title': 'Kommunikationsfähigkeit',
                'description': 'Kommunikationsmittel zielführend einsetzen. Informationsaustausch glaubwürdig aufbauen und aufrechterhalten. Botschaften klar und wirksam gestalten. Zuhören und Botschaften anderer richtig interpretieren.'
            },
            {
                'title': 'Verhandlungsgeschick',
                'description': 'Zielführend und konstruktiv Einfluss nehmen. Bedürfnissen und Erwartungen des Gegenüber angemessenen begegnen und dabei die eigenen Interessen wahren.'
            },
            {
                'title': 'Networking',
                'description': 'Authentisch in Kontakt treten. Beziehungen und Netzwerke gezielt aufbauen und pflegen. Netzwerke aktivieren und Wissen teilen. In gesundem Mass Selbstinszenierung zeigen.'
            },
            {
                'title': 'Teamfähigkeit',
                'description': 'Wege zur Kooperation zeigen und sich in eine Gruppe integrieren. Mit einer positiven Grundhaltung einen Beitrag zur gemeinsamen Zielerreichung leisten. Eigene Kompetenzen und Fähigkeiten gezielt einbringen.'
            }
        ],
        'modules': [
            {
                'title': 'Effizient kommunizieren',
                'skill': 'Kommunikationsfähigkeiten',
                'teaser': 'Gezieltes Training für Führungsalltag und Verhandlung'
            },
            {
                'title': 'Diversity for Success',
                'skill': 'Konfliktfähigkeit',
                'teaser': 'Wertschöpfender Umgang mit der Vielfalt'
            },
            {
                'title': 'The 1st 100 days',
                'skill': 'Kommunikationsfähigkeit',
                'teaser': 'On-boarding in eine neue Rolle'
            },
            {
                'title': 'The 1st 30 days',
                'skill': 'Networking',
                'teaser': 'On-boarding in eine neue Organisation'
            }
        ]
    }
]


class Command(BaseCommand):

    def ensure_clean_dir(self, folder):
        path = os.path.join(settings.MEDIA_ROOT, folder)
        if os.path.exists(path):
            shutil.rmtree(path)
        if not os.path.exists(path):
            os.makedirs(path)

    def filter_data(self, input_data, filter_keyword):
        filters = [filter_keyword] if not isinstance(filter_keyword, list) else filter_keyword
        return {k: v for (k, v) in input_data.items() if not (k in filters)}

    def handle(self, *args, **options):

        # print(settings.DATABASES)
        # print(settings.DATABASES['default'])
        # print(settings.DATABASES['default']['USER'])
        # return

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

        # module_images = [
        #     ImageField(from_path=os.path.join(settings.BASE_DIR, 'core/static/img/dummy/module_0.png')),
        #     ImageField(from_path=os.path.join(settings.BASE_DIR, 'core/static/img/dummy/module_1.png')),
        #     ImageField(from_path=os.path.join(settings.BASE_DIR, 'core/static/img/dummy/module_2.png')),
        #     ImageField(from_path=os.path.join(settings.BASE_DIR, 'core/static/img/dummy/module_3.png')),
        # ]
        module_images = [
            ImageField(from_path=os.path.join(settings.BASE_DIR, 'core/static/img/modules/modul_board_viola.jpg')),
            ImageField(
                from_path=os.path.join(settings.BASE_DIR, 'core/static/img/modules/modul_frau-computer_viola.png')),
            ImageField(
                from_path=os.path.join(settings.BASE_DIR, 'core/static/img/modules/modul_talk-communikation.jpg')),
            ImageField(
                from_path=os.path.join(settings.BASE_DIR, 'core/static/img/modules/modul_talk_communication_1man.jpg')),
            ImageField(from_path=os.path.join(settings.BASE_DIR, 'core/static/img/modules/modul_way-career.jpg')),
        ]

        u = UserFactory(
            username='test',
            is_staff=True,
            is_superuser=True
        )

        for i in range(0, 4):
            UserFactory(username='user{}'.format(i))

        module_counter = 0
        for idx, category_data in enumerate(data):
            category = CategoryFactory.create(
                parent=site.root_page,
                title=category_data['title'],
                teaser=category_data['teaser'],
                icon_component=category_data['icon'],
                icon__file=category_images[idx % len(category_images)]
            )

            competences = category_data['competences']
            for competence in competences:
                CompetenceFactory.create(
                    title=competence['title'],
                    description=competence['description'],
                    category=category
                ).save()

            default_modules = [{} for i in range(0, 2)]
            modules_data = category_data.get('modules', default_modules)

            for module_idx, module_data in enumerate(modules_data):
                module = ModuleFactory.create(
                    parent=category,
                    hero_image__file=module_images[module_idx % len(module_images)],
                    **self.filter_data(module_data, ['units', 'goals'])
                )

                default_units = [{} for i in range(0, random.randint(3, 5))]
                units_data = module_data.get('units', default_units)
                for unit_data in units_data:
                    UnitFactory.create(parent=module, **unit_data)

                default_goals = [{'level': lvl} for lvl in range(0, 3)]
                goals_data = module_data.get('goals', default_goals)
                for goal_data in goals_data:
                    GoalFactory.create(module=module, **goal_data)

        # create user progress
        UserModuleProgressFactory.create_batch(size=20)
        all_module_progress = UserModuleProgress.objects.all()
        for module_progress in all_module_progress:
            UserUnitProgressFactory.create_batch(size=3, module_progress=module_progress)

        # create user focus
        all_users = get_user_model().objects.all()
        for user in all_users:
            focus = FocusFactory.create(user=user)
            CompetenceEntryFactory.create_batch(size=10, focus=focus)

        # create user goals for users and goals
        UserGoalFactory.create_batch(size=20)

        # create user stuff for testing
        u = UserFactory(
            username='guru',
            is_staff=True,
            is_superuser=True
        )
        u.set_password('oRIbsyYmOy')
        u.save()

        u = UserFactory(
            username='visitor',
            is_staff=True,
            is_superuser=True
        )
        u.set_password('ioatQQKvtK')
        u.save()

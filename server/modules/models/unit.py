from django.db import models
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, FieldRowPanel, TabbedInterface, ObjectList
from wagtail.core.fields import RichTextField

from core.wagtail_utils import StrictHierarchyPage
from modules.blocks import DEFAULT_RICH_TEXT_FEATURES
from modules.models.competence import Competence


class Unit(StrictHierarchyPage):
    class Meta:
        verbose_name = 'Lernangebot'
        verbose_name_plural = 'Lernangebote'

    competences = models.ManyToManyField(Competence)

    teaser = models.TextField(default='')
    lead = models.TextField(default='')
    description = models.TextField(default='')

    objectives = RichTextField(features=DEFAULT_RICH_TEXT_FEATURES)
    content = RichTextField(features=DEFAULT_RICH_TEXT_FEATURES)
    teacher = RichTextField(features=DEFAULT_RICH_TEXT_FEATURES)
    requirements = RichTextField(features=DEFAULT_RICH_TEXT_FEATURES)

    type = models.CharField(
        max_length=100,
        choices=(
            ('webinar', 'Webinar'),
            ('kurs', 'Kurs'),
            ('hybrid', 'Hybrid'),
            ('coaching', 'Coaching'),
            ('tinder', 'Tinder'),
            ('lernfilm', 'Lernfilm'),
            ('webex', 'Webex'),
            ('interaktiv', 'Interaktiv'),
        )
    )
    count = models.CharField(
        max_length=255,
        help_text='e.g. \'3 Veranstaltungen\''
    )
    duration = models.CharField(
        max_length=255,
        help_text='e.g. \'je 2 Tage\''
    )
    price = models.CharField(
        default='',
        max_length=255,
        help_text='e.g. \'CHF 150\''
    )

    content_panels = [
        FieldPanel('title', classname="full title"),
        FieldPanel('teaser'),
        FieldPanel('description'),
        FieldPanel('type'),
        FieldPanel('competences'),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('count'),
                FieldPanel('duration'),
            ], classname="label-above"),
        ], 'Kadenz'),
        FieldPanel('price'),
    ]
    settings_panels = [
        FieldPanel('slug')
    ]
    edit_handler = TabbedInterface([
        ObjectList(content_panels, heading='Content'),
        ObjectList(settings_panels, heading='Settings'),
    ])

    template = 'generic_page.html'

    parent_page_types = ['modules.Module']
    subpage_types = []

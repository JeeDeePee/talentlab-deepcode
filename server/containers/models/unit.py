from django.db import models
from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, FieldRowPanel, TabbedInterface, ObjectList


class Unit(Page):
    teaser = models.TextField()
    type = models.CharField(
        max_length=100,
        choices=(
            ('webinar', 'Webinar'),
            ('kurs', 'Kurs'),
            ('coaching', 'Coaching')
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

    parent_page_types = ['containers.Container']
    subpage_types = []

    content_panels = [
        FieldPanel('title', classname="full title"),
        FieldPanel('teaser'),
        FieldPanel('type'),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('count'),
                FieldPanel('duration'),
            ], classname="label-above"),
        ], 'Kadenz')
    ]
    settings_panels = [
        FieldPanel('slug')
    ]
    edit_handler = TabbedInterface([
        ObjectList(content_panels, heading='Content'),
        ObjectList(settings_panels, heading='Settings'),
    ])

    template = 'generic_page.html'

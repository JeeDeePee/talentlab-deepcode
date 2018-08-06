from django.db import models
from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, FieldRowPanel, TabbedInterface, ObjectList


class Goal(Page):
    class Meta:
        verbose_name = 'Ziel'
        verbose_name_plural = 'Ziele'

    level = models.PositiveIntegerField(default=0, null=True, blank=True, help_text='Ziel-Level')
    goal_text = models.TextField()

    content_panels = [
        FieldPanel('title', classname="full title"),
        FieldPanel('level'),
        FieldPanel('goal_text')
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

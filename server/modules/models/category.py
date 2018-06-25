from django.db import models
from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel, TabbedInterface, ObjectList
from wagtail.images.edit_handlers import ImageChooserPanel


class Category(Page):
    class Meta:
        verbose_name = 'Kategorie'
        verbose_name_plural = 'Kategorien'

    icon = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    subpage_types = ['modules.Module']

    content_panels = [
        FieldPanel('title', classname="full title"),
        ImageChooserPanel('icon')
    ]
    settings_panels = [
        FieldPanel('slug')
    ]
    edit_handler = TabbedInterface([
        ObjectList(content_panels, heading='Content'),
        ObjectList(settings_panels, heading='Settings'),
    ])

    template = 'generic_page.html'

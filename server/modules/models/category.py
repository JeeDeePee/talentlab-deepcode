from django.db import models
from wagtail.admin.edit_handlers import FieldPanel, TabbedInterface, ObjectList
from wagtail.images.edit_handlers import ImageChooserPanel

from core.wagtail_utils import StrictHierarchyPage


class Category(StrictHierarchyPage):
    class Meta:
        verbose_name = 'Kategorie'
        verbose_name_plural = 'Kategorien'

    teaser = models.TextField(default='')
    icon_component = models.CharField(max_length=100, default='EmptyIcon')
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
        FieldPanel('teaser'),
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

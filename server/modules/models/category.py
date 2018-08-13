from django.db import models
from wagtail.admin.edit_handlers import FieldPanel, TabbedInterface, ObjectList
from wagtail.core.models import Page
from wagtail.images.edit_handlers import ImageChooserPanel


class Category(Page):
    class Meta:
        verbose_name = 'Kategorie'
        verbose_name_plural = 'Kategorien'

    teaser = models.TextField(default='')
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

    def get_child_ids(self):
        return self.get_children().values_list('id', flat=True)

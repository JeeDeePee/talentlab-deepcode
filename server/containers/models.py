from django.db import models
from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel

from containers.blocks import RichTextBlock, ImageBlock, DocumentBlock


class Container(Page):
    intro = models.CharField(max_length=250)

    content = StreamField([
        ('text', RichTextBlock()),
        ('image', ImageBlock()),
        ('document', DocumentBlock()),
    ])

    content_panels = Page.content_panels + [
        FieldPanel('intro'),
        StreamFieldPanel('content'),
    ]

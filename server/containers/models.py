from django.db import models
from wagtail.core.blocks.field_block import URLBlock, CharBlock
from wagtail.core.blocks.struct_block import StructBlock
from wagtail.core.models import Page
from wagtail.core.fields import StreamField, RichTextField
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel, MultiFieldPanel, FieldRowPanel, TabbedInterface, \
    ObjectList
from wagtail.images.edit_handlers import ImageChooserPanel

from containers.blocks import RichTextBlock, ImageBlock, DocumentBlock


class Category(Page):
    icon = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    subpage_types = ['containers.Container']

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


class Container(Page):
    # category = models.ForeignKey('containers.Category', on_delete=models.CASCADE, related_name='+')

    skill = models.CharField(
        max_length=255,
        help_text='e.g. \'Leadership\''
    )
    hero_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    teaser = models.TextField()
    description = RichTextField()

    video_id = models.PositiveIntegerField(
        null=True,
        blank=True,
        help_text='Vimeo video id (https://vimeo.com/<this-id>)'
    )
    video_description = models.TextField(
        null=True,
        blank=True
    )

    resources = StreamField([
        ('link', StructBlock([
            ('description', CharBlock()),
            ('url', URLBlock())
        ], icon='link')),
        ('document', StructBlock([
            ('description', CharBlock()),
            ('file', DocumentBlock()),
        ], icon='doc-empty'))
    ],
        null=True,
        blank=True
    )

    tools = StreamField([
        ('link', StructBlock([
            ('description', CharBlock()),
            ('url', URLBlock())
        ], icon='link')),
        ('document', StructBlock([
            ('description', CharBlock()),
            ('file', DocumentBlock())
        ], icon='doc-empty'))
    ],
        null=True,
        blank=True
    )

    parent_page_types = ['containers.Category']
    subpage_types = ['containers.Unit']

    content_panels = [
        FieldPanel('title', classname="full title"),
        FieldPanel('skill'),
        ImageChooserPanel('hero_image'),
        FieldPanel('teaser'),
        FieldPanel('description'),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('video_id'),
                FieldPanel('video_description'),
            ], classname="label-above"),
        ], 'Video'),
        StreamFieldPanel('resources'),
        StreamFieldPanel('tools')
    ]

    settings_panels = [
        FieldPanel('slug')
    ]

    edit_handler = TabbedInterface([
        ObjectList(content_panels, heading='Content'),
        ObjectList(settings_panels, heading='Settings'),
    ])


class Unit(Page):
    # container = models.ForeignKey('containers.Container', on_delete=models.CASCADE, related_name='+')

    teaser = models.TextField()
    type = models.CharField(
        max_length=100,
        choices=(
            ('Webinar', 'Webinar'),
            ('Kurs', 'Kurs'),
            ('Coaching', 'Coaching')
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

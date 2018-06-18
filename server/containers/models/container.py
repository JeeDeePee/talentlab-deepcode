from django.contrib.postgres.fields import JSONField
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from wagtail.core.models import Page
from wagtail.core.fields import StreamField, RichTextField
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel, MultiFieldPanel, FieldRowPanel, TabbedInterface, \
    ObjectList
from wagtail.documents.models import Document
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.images.models import Image

from containers.blocks import LinkBlock, DocumentBlock, DEFAULT_RICH_TEXT_FEATURES


class Container(Page):
    hero_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    skill = models.CharField(
        max_length=255,
        help_text='e.g. \'Leadership\''
    )
    teaser = models.TextField()
    description = RichTextField(features=DEFAULT_RICH_TEXT_FEATURES)

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
        ('link', LinkBlock(icon='link')),
        ('document', DocumentBlock(icon='doc-empty'))
    ],
        null=True,
        blank=True
    )
    resources_normalized = JSONField(blank=True, null=True, help_text='helper field for graphql api')

    tools = StreamField([
        ('link', LinkBlock(icon='link')),
        ('document', DocumentBlock(icon='doc-empty'))
    ],
        null=True,
        blank=True
    )
    tools_normalized = JSONField(blank=True, null=True, help_text='helper field for graphql api')

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

    template = 'generic_page.html'


@receiver(pre_save, sender=Container)
def pre_save_container(sender, instance, **kwargs):
    def nomralize_data(field):
        data = []
        for d in field.stream_data:

            if isinstance(d, dict):
                _type = d['type']
                value = dict(d['value'])
                if 'document' in value:
                    value['document'] = Document.objects.get(id=value['document']).file.url
                if 'image' in value:
                    value['image'] = Image.objects.get(id=value['image']).file.url
            else:
                _type = d[0]
                value = dict(d[1])
                if 'document' in value:
                    value['document'] = value['document'].file.url
                if 'image' in value:
                    value['image'] = value['image'].file.url

            data.append({
                'type': _type,
                'value': value
            })
        return data

    instance.tools_normalized = nomralize_data(instance.tools)
    instance.resources_normalized = nomralize_data(instance.resources)

import logging

import requests
from django.contrib.postgres.fields import JSONField
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel, MultiFieldPanel, FieldRowPanel, TabbedInterface, \
    ObjectList
from wagtail.core.fields import StreamField, RichTextField
from wagtail.documents.models import Document
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.images.models import Image

from core.wagtail_utils import StrictHierarchyPage
from modules.blocks import LinkBlock, DocumentBlock, DEFAULT_RICH_TEXT_FEATURES

logger = logging.getLogger(__name__)


class Module(StrictHierarchyPage):
    class Meta:
        verbose_name = 'Lernmodul'
        verbose_name_plural = 'Lernmodule'

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
    lead = models.TextField()
    description = RichTextField(features=DEFAULT_RICH_TEXT_FEATURES)

    video_id = models.PositiveIntegerField(
        null=True,
        blank=True,
        help_text='Vimeo video id (https://vimeo.com/<this-id>)'
    )
    video_description = RichTextField(
        features=DEFAULT_RICH_TEXT_FEATURES,
        null=True,
        blank=True
    )
    video_thumbnail_data = JSONField(null=True, blank=True)

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

    parent_page_types = ['modules.Category']
    subpage_types = ['modules.Unit']

    def get_child_ids(self):
        return self.get_children().values_list('id', flat=True)


VIMEO_META_URL = 'https://vimeo.com/api/oembed.json?url=https%3A//vimeo.com/{video_id}'


@receiver(pre_save, sender=Module)
def pre_save_module(sender, instance, **kwargs):
    def normalize_data(field):
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

    instance.tools_normalized = normalize_data(instance.tools)
    instance.resources_normalized = normalize_data(instance.resources)

    try:
        if instance.video_id:
            res = requests.get(url=VIMEO_META_URL.format(video_id=instance.video_id)).json()
            instance.video_thumbnail_data = {k: v for (k, v) in res.items() if k.startswith('thumbnail')}
        else:
            instance.video_thumbnail_data = {}
    except:
        logger.exception('Could not get vimeo video data')
        instance.video_thumbnail_data = {}

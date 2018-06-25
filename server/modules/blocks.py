from wagtail.core import blocks
from wagtail.documents.blocks import DocumentChooserBlock

DEFAULT_RICH_TEXT_FEATURES = ['bold', 'italic', 'link', 'ol', 'ul']


class LinkBlock(blocks.StructBlock):
    url = blocks.URLBlock()
    description = blocks.CharBlock()


class DocumentBlock(blocks.StructBlock):
    document = DocumentChooserBlock()
    description = blocks.CharBlock()

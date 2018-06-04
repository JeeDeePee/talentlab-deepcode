from wagtail.core import blocks
from wagtail.documents.blocks import DocumentChooserBlock
from wagtail.images.blocks import ImageChooserBlock

DEFAULT_RICH_TEXT_FEATURES = ['h2', 'h3', 'h4', 'h5', 'h6', 'bold', 'italic', 'link', 'ol', 'ul']


class RichTextBlock(blocks.StructBlock):
    text = blocks.RichTextBlock(features=DEFAULT_RICH_TEXT_FEATURES)


class ImageBlock(blocks.StructBlock):
    image = ImageChooserBlock()
    label = blocks.TextBlock(required=False)


class DocumentBlock(blocks.StructBlock):
    document = DocumentChooserBlock()
    label = blocks.TextBlock(required=False)

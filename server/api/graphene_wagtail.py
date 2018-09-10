# mysite/api/graphene_wagtail.py
# Taken from https://github.com/patrick91/wagtail-ql/blob/master/backend/graphene_utils/converter.py and slightly adjusted

from graphene.types import Scalar
from graphene_django.converter import convert_django_field
from wagtail.core.fields import StreamField
from wagtail.images.models import Image


class GenericStreamFieldType(Scalar):
    @staticmethod
    def serialize(stream_value):
        stream_data = stream_value.stream_data

        for d in stream_data:
            if isinstance(d, dict):
                _type = d['type']
                if _type == 'image_block':
                    _value = d['value']
                    value = {
                        # 'value': _value,
                        # 'id': d['id'],
                        'path': Image.objects.get(id=_value).file.url
                    }
                    d['value'] = value

                # value = dict(d['value'])
                # if 'document' in value:
                #     value['document'] = Document.objects.get(id=value['document']).file.url
                # if 'image' in value:
                #     value['image'] = Image.objects.get(id=value['image']).file.url

            # else:
            #     _type = d[0]
            #     value = dict(d[1])
            #     if 'document' in value:
            #         value['document'] = value['document'].file.url
            #     if 'image' in value:
            #         value['image'] = value['image'].file.url

        return stream_data

        # can we implement a node deserializer which will decode the pk into a url?
        # currently this is implemented in a pre_save hook

        # TODO: implement a ImageNode api representation which can be used in a more OO way
        #
        # by_api = stream_value.stream_block.get_api_representation(stream_value)
        # return by_api


@convert_django_field.register(StreamField)
def convert_stream_field(field, registry=None):
    return GenericStreamFieldType(description=field.help_text, required=not field.null)

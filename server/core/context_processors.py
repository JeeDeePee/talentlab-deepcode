from django.conf import settings


def settings_context(request):
    context = {
        'RAVEN_DSN_JS': settings.RAVEN_DSN_JS,
        'GOOGLE_TAG_MANAGER_CONTAINER_ID': settings.GOOGLE_TAG_MANAGER_CONTAINER_ID,
        'DEBUG': settings.DEBUG
    }
    return context

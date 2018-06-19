from django.conf.urls import url, include
from django.urls import re_path
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from wagtail.core import urls as wagtail_urls
from wagtail.admin import urls as wagtailadmin_urls
from wagtail.documents import urls as wagtaildocs_urls
from wagtail.search import urls as wagtailsearch_urls
from core import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^guru/', admin.site.urls),

    url(r'^cms/', include(wagtailadmin_urls)),
    url(r'^search/', include(wagtailsearch_urls)),
    url(r'^documents/', include(wagtaildocs_urls)),

    url(r'^api/', include('api.urls', namespace="api")),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL,
                                                                        document_root=settings.STATIC_ROOT)

# actually we use the cms in headless mode but need the url pattern to get the wagtail_serve function
urlpatterns += [url(r'pages/', include(wagtail_urls)), ]

urlpatterns += [re_path(r'^.*$', views.home, name='home')]

admin.site.site_header = 'Talentlab Admin'

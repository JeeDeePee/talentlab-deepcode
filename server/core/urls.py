from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from wagtail.core import urls as wagtail_urls
from wagtail.admin import urls as wagtailadmin_urls
from wagtail.documents import urls as wagtaildocs_urls
from wagtail.search import urls as wagtailsearch_urls
from core import views

urlpatterns = [
    url(r'^guru/', admin.site.urls),

    url(r'^cms/', include(wagtailadmin_urls)),
    url(r'^search/', include(wagtailsearch_urls)),
    url(r'^documents/', include(wagtaildocs_urls)),

    url(r'^api/', include('api.urls', namespace="api")),
]

urlpatterns += staticfiles_urlpatterns()

urlpatterns += [url(r'^.*$', views.home, name='home')]

# actually we use the cms in headless mode
#urlpatterns += [url(r'', include(wagtail_urls)), ]

admin.site.site_header = 'Talentlab Admin'

from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import re_path
from wagtail.admin import urls as wagtailadmin_urls
from wagtail.core import urls as wagtail_urls
from django.contrib.auth.views import logout
from core import views

urlpatterns = [
    url(r'^guru/', admin.site.urls),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^logout/$', logout, {'next_page': '/'}, name='logout'),
    url(r'^cms/', include(wagtailadmin_urls)),
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

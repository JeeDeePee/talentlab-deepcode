import requests
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie
from graphene_django.views import GraphQLView
from django.conf import settings


class PrivateGraphQLView(LoginRequiredMixin, GraphQLView):
    pass


@ensure_csrf_cookie
def home(request):
    if settings.DEBUG:
        import socket
        def hostname_resolves(hostname):
            try:
                socket.gethostbyname(hostname)
                return True
            except socket.error:
                return False

        try:
            url = 'http://{}:8080{}'.format(
                'host.docker.internal' if hostname_resolves('host.docker.internal') else 'localhost',
                request.get_full_path())
            r = requests.get(url)
            return HttpResponse(r.text)
        except Exception as e:
            print('Can not connect to dev server at {} ({})'.format(url, e))

    return render(request, 'index.html', {})

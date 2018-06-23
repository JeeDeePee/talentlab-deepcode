import requests
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie
from graphene_django.views import GraphQLView
from django.conf import settings


class PrivateGraphQLView(LoginRequiredMixin, GraphQLView):
    pass


@login_required
@ensure_csrf_cookie
def home(request):
    if settings.DEBUG:
        try:
            return HttpResponse(requests.get('http://localhost:8080/{}'.format(request.get_full_path())).text)
        except Exception as e:
            print('Can not connect to dev server at http://localhost:8080:', e)

    return render(request, 'index.html', {})

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie
from graphene_django.views import GraphQLView


class PrivateGraphQLView(LoginRequiredMixin, GraphQLView):
    pass


@login_required
@ensure_csrf_cookie
def home(request):
    return render(request, 'index.html', {})

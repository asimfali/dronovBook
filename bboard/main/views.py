from django.http import Http404, HttpResponse
from django.shortcuts import render
from django.template.loader import get_template
from django.template import TemplateDoesNotExist
from django.contrib.auth.views import LoginView


def index(request):
    return render(request, 'main/index.html')


def other_page(request, page):
    try:
        template = get_template(f"main/{page}.html")
    except TemplateDoesNotExist:
        raise Http404
    return HttpResponse(template.render(request=request))


class BBLoginView(LoginView):
    template_name = 'main/login.html'

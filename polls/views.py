from django.http import HttpResponse


def index(request):
    return HttpResponse('Hello world. Wou are at polls index page.')

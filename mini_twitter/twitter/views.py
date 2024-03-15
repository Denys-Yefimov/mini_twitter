from django.http import HttpResponse


def index(request):
    print(dir(request))
    return HttpResponse("Hello world!")


def test(request):
    return HttpResponse("<h1>Test title</h1>")

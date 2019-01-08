from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.1")

def index2(request):
    return HttpResponse("Hello, world. You're at the polls index2.")    
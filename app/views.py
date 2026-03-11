from django.http import HttpResponse

# Create your views here.
def helloWorld(request):
    return HttpResponse('<h1>Hello World</h1>')
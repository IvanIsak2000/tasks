from django.shortcuts import render
from django.http import HttpResponse
from .models import Text


def home(request):
    data = Text.objects.all().filter(public=True)
    context = {
    'data': data
    }
    return render(request, 'app1/index.html', context)

def signup(request):
    if request.POST:
        name = request.POST.get('name', 0)
        password = request.POST.get('password', 0)
        print(name, password)
        return HttpResponse(f'{name}:{login}')
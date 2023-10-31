from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'app1/index.html')

def signup(request):
    if request.POST:
        name = request.POST.get('name', 0)
        password = request.POST.get('password', 0)
        print(name, password)
        return HttpResponse(f'{name}:{login}')
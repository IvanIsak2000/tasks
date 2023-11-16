from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from django.contrib.auth import logout as auth_logout


from .models import Text


def home(request):
    try:
        auth_logout(request)
    except:
        pass
    data = Text.objects.all().filter(public=True).order_by('?')
    context = {
    'data': data
    }
    return render(request, 'app1/index.html', context)


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    data = Text.objects.all().order_by('?')
                    context = {
                        'data': data,
                        'username': cd['username']
                    }
                    return render(request, 'app1/index.html', context)
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'app1/account.html', {'form': form})
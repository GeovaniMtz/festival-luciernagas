from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegisterForm

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('explore')
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {'form': form})

def explore_view(request):
    return render(request, 'explore.html')

def mapa(request):
    return render(request, 'mapa.html')

def parques_view(request):
    return render(request, 'parques.html')
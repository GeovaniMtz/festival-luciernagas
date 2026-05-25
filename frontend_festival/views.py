from django.shortcuts import render

def register_view(request):
    return render(request, 'registration/register.html')

def explore_view(request):
    return render(request, 'explore.html')
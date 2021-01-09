from django.shortcuts import render


def info_home(request):
    return render(request, 'info/info_home.html')
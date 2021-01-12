from django.shortcuts import render
from django.contrib.auth.models import User   


def main(request):
    print(request)
    users = User.objects.all()
    print('users: ', users)
    user = request.user
    print('user  : ', user)
    return render(request, 'main/main.html')
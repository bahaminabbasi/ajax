from django.shortcuts import render, HttpResponse


def profile_page(request):
    user = request.user

    return render(request, 'accounts/profile.html', {'user': user})
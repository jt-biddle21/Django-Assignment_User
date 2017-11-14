from django.shortcuts import render, redirect


def index(request):
    return render(request, 'assign_users_app/index.html')

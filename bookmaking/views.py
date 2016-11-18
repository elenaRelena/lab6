from django.shortcuts import render
from .models import User
from django.views import View
from pip._vendor import requests

class user_view(View):
    def get(self,request):
        users = User.objects.all()
        return render (request, 'bookmaking/users.html', {'users': users})


def main_page(request):
    return render (request, 'bookmaking/main_page.html', {})
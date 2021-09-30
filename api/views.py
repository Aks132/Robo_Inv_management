from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import JsonResponse

from django.contrib.auth import authenticate,login

def index(request):
    print("hello")
    if (request.method == 'GET'):
        return render(request, 'index.html')


    if (request.method == 'POST'):
        print('post request')
        username = request.POST.get("username")
        password = request.POST.get("pass")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
        else:
            print('Error')

            response = {'user invalid': 'Error'}
            return JsonResponse(response)

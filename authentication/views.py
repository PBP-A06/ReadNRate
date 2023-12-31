import json
from django.shortcuts import render
from django.contrib.auth import authenticate, login as auth_login
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User

from authentication.forms import RegistrationForm

from rest_framework.authtoken.models import Token

@csrf_exempt
def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            auth_login(request, user)
            token, _ = Token.objects.get_or_create(user=user)
            return JsonResponse({
                "username": user.username,
                "status": True,
                "message": "Login sukses!",
                "token": token.key  # Include the token in the response
            }, status=200)
        else:
            return JsonResponse({
                "status": False,
                "message": "Login gagal, akun dinonaktifkan."
            }, status=401)
        
    else:
        return JsonResponse({
            "status": False,
            "message": "Login gagal, periksa kembali email atau kata sandi."
        }, status=401)
    
@csrf_exempt
def logout(request):
    username = request.user.username

    try:
        auth_logout(request)
        return JsonResponse({
            "username": username,
            "status": True,
            "message": "Logout berhasil!"
        }, status=200)
    except:
        return JsonResponse({
        "status": False,
        "message": "Logout gagal."
        }, status=401)
    
@csrf_exempt
def register(request):
    if request.method != "POST":
        return JsonResponse({
            "status": "failed",
            "message": "Register gagal. Bukan method POST"
            }, status=401)   
    
    data = json.loads(request.body)
    username = data['username']
    password = data['password']
    password_confirmation = data['passwordConfirmation']

    if username == "" or password == "":
            return JsonResponse({
            "status": "failed",
            "message": "Register gagal. Ada fields kosong."
            }, status=401)
    
    if password != password_confirmation:
            return JsonResponse({
            "status": "failed",
            "message": "Register gagal. Password tidak match."
            }, status=401)   
    
    try: 
        user = User.objects.create(
            username = username,
            password = make_password(password),
        )
        user.save()

        return JsonResponse({
            'status': 'success',
            'message': 'Berhasil register',
            }, status=201)
    
    except Exception:
        return JsonResponse({
            "status": "failed",
            "message": f"Register gagal. Sudah ada pengguna dengan username {username}."
            }, status=401)
    
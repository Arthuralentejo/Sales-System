from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserLoginForm

def home(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'home.html', {'form': form})


def user_list(request):
    if request.method == 'POST':
        document_id = request.POST.get('document_id')
        if CustomUser.objects.filter(document_id=document_id).exists():
            messages.error(request, 'Documento já cadastrado')
            return render(request, 'home.html')
        else:
            new_user = CustomUser()
            new_user.first_name = request.POST.get('first_name')
            new_user.last_name = request.POST.get('last_name')
            new_user.document_id = document_id
            new_user.save()
            messages.success(request, 'User registered successfully.')

    users = {
        'users': CustomUser.objects.all()
    }
    return render(request, 'user_list.html', users)

# def register(request):
#     if request.method == 'POST':
#         form = CustomUserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'User registered successfully.')
#             return redirect('login')
#     else:
#         form = CustomUserCreationForm()
#     return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = CustomUserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserLoginForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

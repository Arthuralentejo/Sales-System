from django.shortcuts import render
from django.contrib import messages
from .models import User

def home(request):
    return render(request, 'home.html')


def user_list(request):
    if request.method == 'POST':
        document_id = request.POST.get('document_id')
        if User.objects.filter(document_id=document_id).exists():
            messages.error(request, 'Documento já cadastrado')
            return render(request, 'home.html')
        else:
            new_user = User()
            new_user.first_name = request.POST.get('first_name')
            new_user.last_name = request.POST.get('last_name')
            new_user.document_id = document_id
            new_user.save()
            messages.success(request, 'User registered successfully.')

    users = {
        'users': User.objects.all()
    }
    return render(request, 'user_list.html', users)

from django.shortcuts import render
from .models import User

def home(request):
    return render(request, 'home.html')


def user_list(request):

    new_user = User()
    new_user.first_name = request.POST.get('first_name')
    new_user.last_name = request.POST.get('last_name')
    new_user.document_id = request.POST.get('document_id')
    new_user.save()

    users = {
        'users': User.objects.all()
    }
    return render(request, 'user_list.html', users)

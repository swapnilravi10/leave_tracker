from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.

#home
def home(request):
    return render(request, 'home.html')

#register
def register(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            user = User.objects.create_user(first_name = firstname , last_name=lastname, username=username, password=password1)
            user.save()
            print('user saved')
            return redirect('/')
        else:
           messages.info(request,'Password did not match')
           return redirect('register')    
    else:
        return render(request, 'register')

        #changes
from django.shortcuts import render
from django.shortcuts import render,redirect
from validate_email import validate_email
from django.contrib import messages
from django.contrib.auth import authenticate,login 
from .models import User
from django.urls import reverse
# Create your views here.
def index(request):

    return render(request, 'index.html')

def register(request):
    if request.method == "POST":
        context = {'has_error': False, 'data': request.POST}
        email = request.POST.get('email')
        idnumber = request.POST.get('idnumber')
        phonenumber = request.POST.get('phonenumber')      
        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if len(password)<6:
                messages.add_message(request,messages.ERROR, 'Password should be atleast 6 characters')

                context['has_error'] = True

        if password != password2 :

                messages.add_message(request,messages.ERROR, 'Passwod 1 and Password 2 do not match')

                context['has_error'] = True

        if not validate_email(email):
                messages.add_message(request,messages.ERROR, 'Enter a valid email address')

                context['has_error'] = True
        if not username:
                messages.add_message(request,messages.ERROR, 'username is required')

                context['has_error'] = True
         
        if User.objects.filter(idnumber = idnumber ).exists():
                messages.add_message(request,messages.ERROR, 'Username is taken, please choose another one')

                context['has_error'] = True


                return render(request, 'authentication/register.html', context,status = 409)
        if context['has_error'] :
                return render(request, 'authentication/register.html', context)

        User.objects.create_user(username = username, email = email, idnumber = idnumber,phonenumber=phonenumber)

        return redirect('login')

    return render(request, 'authentication/register.html')



def login_user(request):
    if request.method == 'POST':
        context ={'data' : request.POST}
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request,username=username ,password=password)
        '''
            if user and not user.is_email_verified :
                messages.add_message(request, messages.ERROR, 'Email is not verified, please check your email inbox')
                return render(request,'authentication/login.html', context)
        '''
        if not user:

            messages.add_message(request,messages.ERROR, 'inavalid credentials')

            return render(request, 'authentication/login.html', context)
            
        login(request, user)

        messages.add_message(request, messages.SUCCESS, f'Welcome {user.username}')
            
        return redirect(reverse('home'))
    
    return render(request, 'authentication/login.html')
# Create your views here.

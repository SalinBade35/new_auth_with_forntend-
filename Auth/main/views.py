# from django.shortcuts import render, redirect

# # Create your views here.
# def index(request):
#     return render(request, "main/index.html")


# from django.contrib import messages
# from django.contrib.auth.models import User
# from django.core.exceptions import ValidationError
# from django.contrib.auth.password_validation import validate_password
# import re  # Import the regular expression module

# from django.contrib.auth.password_validation import validate_password
# from django.core.exceptions import ValidationError
# from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm
# # from .models import User
# from django.contrib import messages


# def register(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         first_name = request.POST['first_name']
#         last_name = request.POST['last_name']
#         email = request.POST['email']
#         password = request.POST['password']
#         confirm_password = request.POST['confirm_password']

#         # Check if passwords match
#         if password == confirm_password:
#             try:
#                 # Check if the email ends with @gmail.com
#                 if not email.endswith('@gmail.com'):
#                     messages.error(request, 'Please enter a valid Gmail address!!!')
#                     return redirect('register')

#                 # Check if username or email already exists
#                 if User.objects.filter(username=username).exists():
#                     messages.error(request, 'Username already exists!!!')
#                     return redirect('register')
                
#                 elif User.objects.filter(email=email).exists():
#                     messages.error(request, 'Email already exists!!!')
#                     return redirect('register')

#                 # Password strength checks
#                 # if len(password) < 8:
#                 #     messages.error(request, 'Password must be at least 8 characters long!!!')
#                 #     return redirect('register')
#                 # elif not re.search(r'[A-Z]', password):
#                 #     messages.error(request, 'Password must contain at least one uppercase letter!!!')
#                 #     return redirect('register')
#                 # elif not re.search(r'[0-9]', password):
#                 #     messages.error(request, 'Password must contain at least one numeric digit!!!')
#                 #     return redirect('register')
#                 # elif not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
#                 #     messages.error(request, 'Password must contain at least one special character!!!')
#                 #     return redirect('register')
#                 # elif username.lower() in password.lower():
#                 #     messages.error(request, 'Password must not contain the username!!!')

#                 # Validate password strength using Django's built-in validation
#                 validate_password(password)

#                 # Create the user
#                 User.objects.create_user(
#                     username=username,
#                     first_name=first_name,
#                     last_name=last_name,
#                     email=email,
#                     password=password
#                 )
#                 # Display a thank you message with the username
#                 messages.success(request, f'Thank you for registering, {username}!!!')
#                 return redirect('log_in')

#             except ValidationError as e:
#                 for error in e.messages:
#                     messages.error(request, error)
#                 return redirect('register')
#         else:
#             messages.error(request, 'Passwords do not match!!!')
#             return redirect('register')

#     return render(request, 'auth/register.html')
#     # return render(request, 'sam/register.html')

# #  by specifying return redirect('page_name'), we're also specify where the message will appear.

# def log_in(request):
#     if request.method=="POST":
#         username=request.POST['username']
#         password=request.POST['password']
#         remember_me = request.POST.get('remember_me') # T or F

#         if not User.objects.filter(username=username):
#             messages.error(request,"Username does not exist")
#             return redirect('log_in')
#         else:
#             user=authenticate(username=username,password=password)
#             if user is not None:
#                 login(request,user)
#                 if remember_me:
#                     request.session.set_expiry(592200) # for 7 days 
#                 else:
#                     request.session.set_expiry(0)
#                 messages.success(request,"login successful")
#                 return redirect('index')
#             else:
#                 messages.error(request,"Incorrect Password")
#                 return redirect('log_in')
#     return render(request,'auth/login.html')

# def log_out(request):
#     logout(request)
#     return redirect('log_in')
    


# @login_required(login_url='log_in')
# def change_password(request):
#     form=PasswordChangeForm(user=request.user)
#     if request.method=='POST':
#         form=PasswordChangeForm(user=request.user,data=request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('log_in')      
    
#     return render(request,'auth/change_password.html',{'form':form})

# @login_required
# def user_profile(request):
#     return render(request, 'auth/user_profile.html')
















from django.shortcuts import render, redirect

from django.contrib import messages
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password
import re  # Import the regular expression module

from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm
from django.contrib import messages


# _____________________________________________________________________________________________________________

def index(request):
    return render(request, "main/index.html")



def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        # Check if passwords match
        if password == confirm_password:
            try:
                # Check if the email ends with @gmail.com
                if not email.endswith('@gmail.com'):
                    messages.error(request, 'Please enter a valid Gmail address!!!')
                    return redirect('register')

                # Check if username or email already exists
                if User.objects.filter(username=username).exists():
                    messages.error(request, 'Username already exists!!!')
                    return redirect('register')
                
                elif User.objects.filter(email=email).exists():
                    messages.error(request, 'Email already exists!!!')
                    return redirect('register')

                # Password strength checks
                # if len(password) < 8:
                #     messages.error(request, 'Password must be at least 8 characters long!!!')
                #     return redirect('register')
                # elif not re.search(r'[A-Z]', password):
                #     messages.error(request, 'Password must contain at least one uppercase letter!!!')
                #     return redirect('register')
                # elif not re.search(r'[0-9]', password):
                #     messages.error(request, 'Password must contain at least one numeric digit!!!')
                #     return redirect('register')
                # elif not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
                #     messages.error(request, 'Password must contain at least one special character!!!')
                #     return redirect('register')
                # elif username.lower() in password.lower():
                #     messages.error(request, 'Password must not contain the username!!!')

                # Validate password strength using Django's built-in validation
                validate_password(password)

                # Create the user
                User.objects.create_user(
                    username=username,
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                    password=password
                )
                # Display a thank you message with the username
                messages.success(request, f'Thank you for registering, {username}!!!')
                return redirect('log_in')

            except ValidationError as e:
                for error in e.messages:
                    messages.error(request, error)
                return redirect('register')
        else:
            messages.error(request, 'Passwords do not match!!!')
            return redirect('register')

    return render(request, 'sam/register.html')
    # return render(request, 'sam/register.html')

#  by specifying return redirect('page_name'), we're also specify where the message will appear.

def log_in(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        remember_me = request.POST.get('remember_me') # T or F

        if not User.objects.filter(username=username):
            messages.error(request,"Username does not exist")
            return redirect('log_in')
        else:
            user=authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                if remember_me:
                    request.session.set_expiry(592200) # for 7 days 
                else:
                    request.session.set_expiry(0)
                messages.success(request,"login successful")
                return redirect('index')
            else:
                messages.error(request,"Incorrect Password")
                return redirect('log_in')
    return render(request,'sam/login.html')

def log_out(request):
    logout(request)
    return redirect('log_in')
    


@login_required(login_url='log_in')
def change_password(request):
    form=PasswordChangeForm(user=request.user)
    if request.method=='POST':
        form=PasswordChangeForm(user=request.user,data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('log_in')      
    
    return render(request,'sam/change_password.html',{'form':form})

@login_required
def user_profile(request):
    return render(request, 'auth/user_profile.html')











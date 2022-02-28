from django.shortcuts import render
# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import login,authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User


from .forms import UserRegistrationForm, LoginForm

def home(request):
    return render(request, 'users/home.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, f'Your account has been created. You can log in now!')    
            return redirect('login')
    else:
        form = UserRegistrationForm()

    context = {'form': form}
    return render(request, 'users/register.html', context)


def login_view(request):
    userlogin = request.user
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username_var = form.cleaned_data.get('username') 
        password_var = form.cleaned_data.get('password')   
        user_profile = User.objects.filter(username=username_var) 
        user = authenticate(request, username = username_var, password = password_var)
        
        if len(user_profile) < 1:
            messages.warning(request, "This user does not exist!")
        try:
            user_profile = User.objects.get(username=username_var)
        except:
            user_profile = None
        
        if user_profile is not None and not user_profile.check_password(password_var):
            messages.warning(request, "wrong password")
        elif user_profile is None:
            pass
        if user:
            login(request, user)
            messages.success(request, "Welcome" + " " + str(userlogin))
            return redirect('/')
        context= {"form": form}
        return render(request, 'auth/login.html', context)


def logout_view(request):
    logout(request)
    return redirect('/login')
  

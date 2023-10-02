from django.shortcuts import render,redirect,reverse
from .forms import LoginForm,CreateUserForm
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User
from .models import Profile

def login_page(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            url = reverse('home')
            return redirect(url)
        else:
            return render(request, 'accounts/login.html', {'error': 'Invalid credentials','form':LoginForm})
        
    else:
        return render(request,'accounts/login.html',{'form':LoginForm})
    
def register_user(request):  
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        number = request.POST['number']
        f_name = request.POST['firstname']
        l_name = request.POST['lastname']
        password = request.POST['password']
        confirm_password = request.POST['confirmpassword']
        if password==confirm_password:
            if User.objects.filter(username=username).exists():
                return render(request,'accounts/register.html',{'error':'Username Already Taken','form':CreateUserForm})
            user = User.objects.create_user(username=username,email=email,first_name=f_name,last_name=l_name,password=password)
            user.backend="django.contrib.auth.backends.ModelBackend"
            user.save()
            profile = Profile.objects.create_profile(user=user,mobile_number=number)
            
            profile.save()
            login(request,user)
            return redirect(reverse('home'))
        else:
            return render(request,'accounts/register.html',{'error':'Password do not match','form':CreateUserForm})
    else:
        return render(request,'accounts/register.html',{'form':CreateUserForm})
        
def logout_page(request):
    logout(request)
    return redirect(reverse('home'))

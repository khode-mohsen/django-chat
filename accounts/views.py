from django.shortcuts import render , HttpResponse , get_object_or_404 , redirect
from django.contrib.auth import authenticate , login ,logout
from django.contrib.auth.forms import AuthenticationForm
from accounts.forms import NewUserForm
# Create your views here.
def register_request(request):
    form = NewUserForm(request.POST or None)
    if request.method =='POST':
        if form.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()
            return redirect('accounts/login.html')
        else:
            print('register failed :: ',form.errors)
            ctx = {'form':form , 'error':form.errors}
            return render(request, 'accounts/register.html', context =ctx)
    else:
        form = NewUserForm()
        return render(request, 'accounts/register.html', context ={'form':form})

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request , data=request.POST)
        if  form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            print(f'login with {username} :: {password}')
            user = authenticate(username= username , password = password)
            if user is not None:
                login(request , user)
                print( f' sucess :: you are logged in as {username}')
                return redirect('/')
            else:
                print('error :: invalid username or password')
        else:
            print('error :: invalid form data')
            return render(request , 'login.html' , context = {'error':'usename or password is wrong !','form':form})

    form = AuthenticationForm()
    return render(request , 'accounts/login.html' , context = {'form' : form})

def logout_request(request):
    logout(request)
    return redirect('/')

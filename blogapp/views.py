from django.shortcuts import render, redirect
from django.views.generic import CreateView, FormView
from blogapp.models import User, Blogs
from blogapp.forms import UserRegistrationForm, LoginForm
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout


def homeView(request):
    return render(request, 'home.html')

class SignUpView(CreateView):
    form_class=UserRegistrationForm
    template_name = 'signup.html'
    model=User
    success_url = reverse_lazy('signin')


class LoginView(FormView):
    form_class = LoginForm
    template_name='signin.html'
    
    def post(self,request,*args,**kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            print('success')
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'signin.html', {'form' : self.form_class})

def signoutView(request,*args,**kwargs):
    logout(request)
    return redirect('signin')
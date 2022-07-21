from urllib import request
from django.shortcuts import render, redirect
from django.views.generic import CreateView, FormView
from django.views import View
from blogapp.models import User, Blogs, Comments
from blogapp.forms import BlogsForm, CommentForm, UserRegistrationForm, LoginForm
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import JsonResponse


class HomeView(CreateView):
    model=Blogs
    form_class = BlogsForm
    template_name ='home.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        self.object = form.save()
        messages.success(self.request,'post updated')
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        blogs = Blogs.objects.all().order_by('-updated_at')
        try:
            Blogs.objects.get(liked_by = self.request.user)
            is_liked = True
        except:
            is_liked = False
        context['blogs'] = blogs
        comment_form = CommentForm()
        context['comment_form'] = comment_form
        context['is_liked'] = is_liked
        return context

def addcommentView(request,*args,**kwargs):
    if request.method =='POST':
        blog_id = request.POST.get('blog_id')
        blog = Blogs.objects.get(id=blog_id)
        user=request.user
        comment = request.POST.get('comment')
        Comments.objects.create(
            blog = blog,
            user = user,
            comment = comment)
        messages.success(request,'comment added successfully')
        return JsonResponse({'suucess' : 'comment added'})

def likeView(request):
    if request.method == 'POST':
        blog_id = request.POST.get('blog_id')
        blog = Blogs.objects.get(id=blog_id)
        blog.liked_by.add(request.user)
        return JsonResponse({'suucess' : 'liked'})

def unlikeView(request):
    if request.method == 'POST':
        blog_id = request.POST.get('blog_id')
        blog = Blogs.objects.get(id=blog_id)
        blog.liked_by.remove(request.user)
        return JsonResponse({'suucess' : 'unliked'})


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
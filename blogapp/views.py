from django.shortcuts import render, redirect
from django.views.generic import CreateView, FormView
from django.views import View
from blogapp.models import User, Blogs, Comments, UserProfile
from blogapp.forms import (BlogsForm, CommentForm, UserRegistrationForm,
 LoginForm, ProfileForm, ProfilePicForm)
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import JsonResponse
from django.db.models import Q


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
        context['blogs'] = blogs
        comment_form = CommentForm()
        context['comment_form'] = comment_form
        return context

def searchBlogView(request):
    search_input = request.GET.get('search-input')
    blogs = Blogs.objects.filter(
        Q(title__icontains = search_input) | 
        Q(description__icontains = search_input) | 
        Q(user__username__icontains = search_input))
    return render(request, 'search.html', {'blogs' : blogs})

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

def removeFollowerView(request):
    if request.method == 'POST':
        follower_user_id = request.POST.get('follower_user_id')
        follower_user = User.objects.get(id=follower_user_id)
        follower_user_profile = UserProfile.objects.get(user = follower_user)
        follower_user_profile.following.remove(request.user)
        follower_user_profile.save()

        remove_request_user_profile = request.user.user_profile
        remove_request_user_profile.followers.remove(follower_user)
        remove_request_user_profile.save()

        return JsonResponse({'suucess' : 'followed'})

def unfollowView(request):
    if request.method == 'POST':
        following_user_id = request.POST.get('following_user_id')
        following_user = User.objects.get(id=following_user_id)
        following_user_profile = UserProfile.objects.get(user = following_user)
        following_user_profile.followers.remove(request.user)
        following_user_profile.save()

        unfollow_request_user_profile = request.user.user_profile
        unfollow_request_user_profile.following.remove(following_user)
        unfollow_request_user_profile.save()

        return JsonResponse({'suucess' : 'followed'})

def followView(request):
    if request.method == 'POST':
        follow_user_id = request.POST.get('follow_user_id')
        follow_user = User.objects.get(id=follow_user_id)
        follow_user_profile = UserProfile.objects.get(user = follow_user)
        follow_user_profile.followers.add(request.user)
        follow_user_profile.save()

        follow_request_user_profile = request.user.user_profile
        follow_request_user_profile.following.add(follow_user)
        follow_request_user_profile.save()

        return JsonResponse({'suucess' : 'followed'})


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

class MyProfileView(View):

    def get(self, request):
        return render(request, 'my_profile.html')

    def post(self, request):
        form = ProfilePicForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            print(request.POST)
            return redirect('my-profile')

 

class ProfileAddView(CreateView):
    try:
        def get(self, request):
            profile = UserProfile.objects.get(user = request.user)
            form = ProfileForm(instance=profile)
            return render(request, 'profile_add.html', {'form' : form})
        
        def post(self, request):
            profile = UserProfile.objects.get(user = request.user)
            form = ProfileForm(request.POST, instance=profile)
            if form.is_valid():
                form.save()
                return render(request, 'my_profile.html')
    except:
        form_class = ProfileForm
        template_name = 'profile_add.html'
        model = UserProfile
        success_url = reverse_lazy('my-profile')

        def form_valid(self, form):
            form.instance.user = self.request.user
            self.object = form.save()
            messages.success(self.request,'post updated')
            return super().form_valid(form)


def otherProfileView(request, *args, **kwargs):
    user_id = kwargs.get('user_id')
    user = User.objects.get(id = user_id)
    return render(request, 'other-profile.html', {'user' : user})

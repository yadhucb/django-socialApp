from urllib import request
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
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

@method_decorator(login_required(login_url='signin'), name='dispatch')
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

@method_decorator(login_required(login_url='signin'), name='dispatch')
class BlogEditView(View):

    def get(self, request, *args, **kwargs):
        blog_id = kwargs.get('id')
        blog = Blogs.objects.get(id = blog_id)
        context = {
        'form' : BlogsForm(instance=blog)
        }

        return render(request, 'blog_edit.html', context)

    def post(self, request, *args, **kwargs):
        blog_id = kwargs.get('id')
        blog = Blogs.objects.get(id = blog_id)
        form = BlogsForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('home')

@login_required(login_url='signin')
def blogDeleteView(request, *args, **kwargs):
    blog_id = kwargs.get('id')
    blog = Blogs.objects.get(id = blog_id)
    blog.delete()
    return redirect('home')

@login_required(login_url='signin')
def searchBlogView(request):
    search_input = request.GET.get('search-input')
    blogs = Blogs.objects.filter(
        Q(title__icontains = search_input) | 
        Q(description__icontains = search_input) | 
        Q(user__username__icontains = search_input) |
        Q(related_language__icontains = search_input)).order_by('-updated_at')
    return render(request, 'search.html', {'blogs' : blogs})

@login_required(login_url='signin')
def filterByLanguageView(request, *args, **kwargs):
    language = kwargs.get('slug')
    blogs = Blogs.objects.filter(related_language__iexact = language)
    context = {
        'blogs' : blogs,
        'comment_form' : CommentForm(),
        'no_blog_post' : True
    }
    return render(request, 'home.html', context)

@login_required(login_url='signin')
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

@method_decorator(login_required(login_url='signin'), name='dispatch')
class CommentEditView(View):

    comment = None

    def get(self, request):
        comment_id = request.GET.get('comment_id')
        global comment
        comment = Comments.objects.get(id = comment_id)
        data = {
            'comment' : comment.comment
        }
        print(data)
        return JsonResponse(data)

    def post(self, request):
        instance = comment
        comment_input = request.POST.get('comment')
        instance.comment = comment_input
        instance.save()
        messages.success(request,'comment edited successfully')
        return JsonResponse({'suucess' : 'comment edited'})

@login_required(login_url='signin')
def deletecommentView(request,*args,**kwargs):
    comment_id = request.GET.get('comment_id')
    comment = Comments.objects.get(id = comment_id)
    comment.delete()
    messages.success(request,'comment deleted successfully')
    return JsonResponse({'suucess' : 'comment deleted'})

@login_required(login_url='signin')
def likeView(request):
    if request.method == 'POST':
        blog_id = request.POST.get('blog_id')
        blog = Blogs.objects.get(id=blog_id)
        blog.liked_by.add(request.user)
        return JsonResponse({'suucess' : 'liked'})

@login_required(login_url='signin')
def unlikeView(request):
    if request.method == 'POST':
        blog_id = request.POST.get('blog_id')
        blog = Blogs.objects.get(id=blog_id)
        blog.liked_by.remove(request.user)
        return JsonResponse({'suucess' : 'unliked'})

@login_required(login_url='signin')
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

@login_required(login_url='signin')
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

@login_required(login_url='signin')
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

@login_required(login_url='signin')
def signoutView(request,*args,**kwargs):
    logout(request)
    return redirect('signin')

@method_decorator(login_required(login_url='signin'), name='dispatch')
class MyProfileView(View):

    def get(self, request):
        return render(request, 'my_profile.html')

    def post(self, request):
        form = ProfilePicForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            print(request.POST)
            return redirect('my-profile')

 
@method_decorator(login_required(login_url='signin'), name='dispatch')
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

@login_required(login_url='signin')
def otherProfileView(request, *args, **kwargs):
    user_id = kwargs.get('user_id')
    user = User.objects.get(id = user_id)
    return render(request, 'other-profile.html', {'user' : user})

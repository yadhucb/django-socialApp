from django import forms
from django.contrib.auth.forms import UserCreationForm
from blogapp.models import User, Blogs, Comments, UserProfile

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=[
            'first_name',
            'last_name',
            'email',
            'username',
            'password1',
            'password2',
        ]

class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField()

class ProfilePicForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['profile_pic',]


class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['bio', 'mobile', 'dob', 'gender']

class BlogsForm(forms.ModelForm):
    class Meta:
        model=Blogs
        fields=[
            'title',
            'description',
            'image',
        ]

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comments
        fields=[
            'comment',
        ]
        widgets={
            'comments':forms.TextInput()
        }
from django import forms
from django.contrib.auth.forms import UserCreationForm
from blogapp.models import User, Blogs, Comments

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
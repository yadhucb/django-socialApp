from django.urls import path
from blogapp import views
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('accounts/signup',views.SignUpView.as_view(), name='signup'),
    path('accounts/sigin',views.LoginView.as_view(), name='signin'),
    path('accounts/signout',views.signoutView, name='signout'),


]
from django.urls import path
from blogapp import views
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('accounts/signup',views.SignUpView.as_view(), name='signup'),
    path('accounts/sigin',views.LoginView.as_view(), name='signin'),
    path('accounts/signout',views.signoutView, name='signout'),

    path('blog/add-comment/', views.addcommentView, name= 'add-comment'),
    path('blog/like/', views.likeView),
    path('blog/unlike/', views.unlikeView),

    path('blog/add-comment/', views.addcommentView, name= 'search'),

    path('user/profile', views.MyProfileView.as_view(), name='my-profile'),
    path('user/profile-add/', views.ProfileAddView.as_view(), name='profile-add'),
    path('other/profile/<str:user_id>', views.otherProfileView, name='other-profile'),


    path('user/follow/', views.followView),
    path('user/remove-follower/', views.removeFollowerView),
    path('user/unfollow/', views.unfollowView),


]
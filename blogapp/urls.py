from django.urls import path
from blogapp import views
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('blog-edit/<int:id>', views.BlogEditView.as_view(), name='blog-edit'),
    path('blog-delete/<int:id>',views.blogDeleteView, name='blog-delete'),

    path('accounts/signup',views.SignUpView.as_view(), name='signup'),
    path('accounts/sigin',views.LoginView.as_view(), name='signin'),
    path('accounts/signout',views.signoutView, name='signout'),

    path('blog/like/', views.likeView),
    path('blog/unlike/', views.unlikeView),

    path('blog/search/', views.searchBlogView, name= 'search-blogs'),
    path('blog/language/<str:slug>', views.filterByLanguageView, name= 'language'),

    path('user/profile', views.MyProfileView.as_view(), name='my-profile'),
    path('user/profile-add/', views.ProfileAddView.as_view(), name='profile-add'),
    path('other/profile/<str:user_id>', views.otherProfileView, name='other-profile'),


    path('user/follow/', views.followView),
    path('user/remove-follower/', views.removeFollowerView),
    path('user/unfollow/', views.unfollowView),


]
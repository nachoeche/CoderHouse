from django.urls import path
from .views import UserRegisterView,UserEditView,ShowProfilePageView,EditProfilePageView,CreateProfilePageView
#Used to use certain views innit in django
from django.contrib.auth import views as auth_views
#password_variable=path("<int:uid>/password/",auth_views.PasswordChangeView.as_view(template_name='registration/change-password'))

urlpatterns = [
    #path("",views.home,name="home"),
    path("register/",UserRegisterView.as_view(),name='register'),
    path("edit_profile/",UserEditView.as_view(),name='edit_profile'),
    path("<int:pk>/profile/",ShowProfilePageView.as_view(),name='show_profile_page'),
    #path("<int:uid>/password/",auth_views.PasswordChangeView.as_view(),name='change_pass'),
    path("<int:pk>/edit_profile_page/",EditProfilePageView.as_view(),name='edit_profile_page'),
    path("create_profile_page/",CreateProfilePageView.as_view(),name='create_profile_page'),
]


from typing import Any
from django.db import models
from django.shortcuts import render
from django.views import generic
#Default forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm,PasswordChangeForm
from django.urls import reverse_lazy
from .forms import SignUpForm,UpdateUserForm,ProfilePageFrom
from django.views.generic import DetailView
from django.shortcuts import render,get_object_or_404
from theblog.models import UserProfile
# Create your views here.

class UserRegisterView(generic.CreateView):
    form_class=SignUpForm
    template_name='registration/register.html'
    success_url=reverse_lazy('login')

class UserEditView(generic.UpdateView):
    form_class=UpdateUserForm
    template_name='registration/edit_profile.html'
    success_url=reverse_lazy('home')

    def get_object(self):
        return self.request.user

class ShowProfilePageView(DetailView):
    model=UserProfile
    template_name='registration/user_profile.html'
    def get_context_data(self, *args, **kwargs):
        users = UserProfile.objects.all()
        context = super(ShowProfilePageView, self).get_context_data(*args, **kwargs)
        page_user=get_object_or_404(UserProfile, id=self.kwargs['pk'])
        post_data = get_object_or_404(UserProfile, id=self.kwargs['pk'])
        context["page_user"]=page_user
        return context
    
class EditProfilePageView(generic.UpdateView):
    model=UserProfile
    template_name='registration/edit_profile_page.html'
    fields=['bio', 'profile_pic', 'facebook_url', 'instagram_url', 'linkedin_url']
    success_url=reverse_lazy('home')

class CreateProfilePageView(generic.CreateView):
    model=UserProfile
    template_name='registration/create_user_profile_page.html'
    form_class=ProfilePageFrom
    
    #Make user id available for the form
    def form_valid(self,form):
        form.instance.user=self.request.user
        return super().form_valid(form)
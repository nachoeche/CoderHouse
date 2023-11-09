from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User
from django import forms
from theblog.models import UserProfile

class SignUpForm(UserCreationForm):
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model=User
        fields=('username','first_name','last_name','email','password1','password2')
    def __init__(self,*args,**kwargs):
        #Since there are some default values, create a innit class to update boostrap
        #Default: username-password1/2
        super(SignUpForm,self).__init__(*args,**kwargs)
        self.fields['username'].widget.attrs['class']='form-control'
        self.fields['password1'].widget.attrs['class']='form-control'
        self.fields['password2'].widget.attrs['class']='form-control'


class UpdateUserForm(UserChangeForm):
    #Wanted fields
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    username=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    #Unwanted fields
    """
    last_login=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    is_superuser=forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-check'}))
    is_staff=forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-check'}))
    is_active=forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-check'}))
    date_joined=forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-check'}))
    """
    class Meta:
        model=User
        #fields=('username','first_name','last_name','email','password','last_login','is_superuser','is_staff','date_joined')
        fields=('username','first_name','last_name','email')
    def __init__(self,*args,**kwargs):
        #Since there are some default values, create a innit class to update boostrap
        #Default: username-password1/2
        super(UpdateUserForm,self).__init__(*args,**kwargs)
        self.fields['username'].widget.attrs['class']='form-control'

class ProfilePageFrom(forms.ModelForm):
    class Meta:
        model=UserProfile
        fields=['bio','profile_pic','facebook_url','instagram_url','linkedin_url']
        widgets={
            'bio': forms.Textarea(attrs={'class': 'form-control'}),
            #'profile_pic': forms.ImageField(attrs={'class': 'form-control'}),
            'facebook_url': forms.TextInput(attrs={'class': 'form-control'}),
            'instagram_url': forms.TextInput(attrs={'class': 'form-control'}),
            #'author': forms.Select(attrs={'class': 'form-control'}),
            'linkedin_url': forms.TextInput(attrs={'class': 'form-control'}),
        }

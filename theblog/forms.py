from django import forms
from .models import Post,Category
from django import forms
#To see all categories on the dropdown, create a ("visuable name", "attribute")
#Setting them in a list so that it's easier to work on
raw_choices=Category.objects.all().values_list('name','name')
cat_choices=[]
for choice in raw_choices:
    cat_choices.append(choice)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields=('title','title_tag','post_resume' , 'author','category', 'body','header_image')
        #Create a widget to define a CSS(boostrap) class to each field
        widgets={
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'post_resume': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control','value': '', 'id':'author_field', 'type':'hidden'}),
            #'author': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=cat_choices,attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            #'header_image': forms.ImageField(attrs={'class': 'form-control'}),
        }
class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields=('title','title_tag','post_resume', 'author','category', 'body')
        #Create a widget to define a CSS(boostrap) class to each field
        widgets={
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'post_resume': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control','value': '', 'id':'author_field', 'type':'hidden'}),
            'category': forms.Select(choices=cat_choices,attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }

#Search bar
class SearchForm(forms.Form):
    query = forms.CharField(max_length=100, label='Search')
from django.db import models
#To connect to the superuser
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime,date
from ckeditor.fields import RichTextField
from django.urls import reverse_lazy,reverse

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=256)
    def __str__(self):
        #Author in str since it's an object
        return self.name
    
    def get_absolute_url(self):
        #Absolute URL of Post will be the post itself
        return reverse("article_details", args=(str(self.id)))
        #This would take to the main page
        #return reverse('home')


class Post(models.Model):
    title=models.CharField(max_length=256)
    header_image=models.ImageField(null=True,blank=True,upload_to="images/")
    #Title that's going to be desplayed on the webpage
    title_tag=models.CharField(max_length=256)
    #delete all posts if user is deleted
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    #Text editor to give format to posts
    body=RichTextField(blank=True, null=True)
    #body=models.TextField()
    post_date=models.DateField(auto_now_add=True)
    category=models.CharField(max_length=256, default='uncategorized')
    #ManyToMany is used to link different clasess
    #It's used hereSince users and posts can have likes
    likes=models.ManyToManyField(User,related_name="blog_posts")
    post_resume=models.CharField(max_length=256)
    def __str__(self):
        #Author in str since it's an object
        return self.title + ' - ' + str(self.author)
    
    def get_absolute_url(self):
        #Absolute URL of Post will be the post itself
        return reverse("article_details", args=(str(self.id)))
        #This would take to the main page
        #return reverse('home')
    
    def total_likes(self):
        return self.likes.count()
    
    
class UserProfile(models.Model):
    #Associate the user module from django with this module.
    user=models.OneToOneField(User,null=True, on_delete=models.CASCADE)
    bio=models.TextField()
    profile_pic=models.ImageField(null=True,blank=True,upload_to="images/profile/")
    facebook_url=models.CharField(max_length=256,null=True,blank=True)
    instagram_url=models.CharField(max_length=256,null=True,blank=True)
    linkedin_url=models.CharField(max_length=256,null=True,blank=True)
    def __str__(self):
        #Author in str since it's an object
        return str(self.user)
    def get_absolute_url(self):
        return reverse('home')
    
class Comment(models.Model):
        post=models.ForeignKey(Post,related_name="comments",on_delete=models.CASCADE)
        name=models.CharField(max_length=255)
        body=models.TextField()
        date_added=models.DateField(auto_now_add=True)

        def __str__(self):
            return f"{self.post.title} - {self.name}"
        
        def get_success_url(self):
            return reverse_lazy('post-detail', kwargs={'pk': self.kwargs['pk']})
        



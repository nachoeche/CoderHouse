from django.contrib import admin
#import Post from models.py
from .models import Post,Category,UserProfile,Comment

# Register your models here.
#This will help to access the Posts from the admin area
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(UserProfile)
admin.site.register(Comment)

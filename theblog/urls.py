from django.urls import path
#from . import views
#As the HomeView is a class, we need to import it.
from .views import HomeView,ArticleDetail,AddPostView,UpdatePostView,DeletePostView,AddCategoryView,CategoryView,LikeView,AddCommentView,AboutUs,EditCommentView,DeleteCommentView

urlpatterns = [
    #path("",views.home,name="home"),
    path("",HomeView.as_view(),name="home"),
    path('about_us/', AboutUs, name='about_us'),
    #This will use a Primary key to refer to the link
    path("article/<int:pk>",ArticleDetail.as_view(),name="article_details"),
    path("add_post/",AddPostView.as_view(),name="add_post"),
    path("article/edit/<int:pk>",UpdatePostView.as_view(),name="update_post"),
    path("article/delete/<int:pk>",DeletePostView.as_view(),name="delete_post"),
    path("add_category/",AddCategoryView.as_view(),name="add_category"),
    path("category/<str:cats>",CategoryView,name="category"),
    path("like/<int:pk>",LikeView,name="like_post"),
    path("article/comment/<int:pk>/",AddCommentView.as_view(),name="add_comment"),
    path('article/edit-comment/<int:pk>/', EditCommentView.as_view(), name='update_comment'),
    path('article/delete-comment/<int:pk>/', DeleteCommentView.as_view(), name='delete_comment'),
]

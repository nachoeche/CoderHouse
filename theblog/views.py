from django.shortcuts import render,get_object_or_404
#ListBiew: brings all Posts 
#DetailView: brings the details from a particular one
#CreateView: To create a post
#UpdateView: To update posts
from django.views.generic import ListView,DetailView, CreateView,UpdateView,DeleteView
from .models import Post,Category,Comment
#Import the form.py file
from .forms import PostForm,EditForm,CommentForm
#Used to redirect while deleting a post
from django.urls import reverse_lazy,reverse
#Used to redirect to same page
from django.http import HttpResponseRedirect
from django.db.models import Sum
#The idea is to be able to click on the titles and move to the particular blog post
#This creates a List for all Posts
from django.db.models import Q

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'posts'
    ordering = ['-post_date']

    def get_queryset(self):
        search_query = self.request.GET.get('query', '')

        if search_query:
            queryset = Post.objects.filter(
                Q(title__icontains=search_query) | 
                Q(body__icontains=search_query)
            ).order_by('-post_date').distinct()
        else:
            queryset = Post.objects.all().order_by('-post_date')

        return queryset

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        search_query = self.request.GET.get('query', '')
        
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        context["search_query"] = search_query
        return context
#This class uses DetailView since it will show a detail for each post.
class ArticleDetail(DetailView):
    model = Post
    template_name = 'article_details.html'
    context_object_name = 'posts'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(ArticleDetail, self).get_context_data(*args, **kwargs)
        post_data = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = post_data.total_likes()
        liked=False
        if post_data.likes.filter(id=self.request.user.id).exists():
            liked=True
        context["cat_menu"] = cat_menu
        context["total_likes"] = total_likes
        context["liked"]=liked
        return context

class AddPostView(CreateView):
    model= Post
    #Import the PostForm from Forms file
    #Since we use this method, we don't have to show them
    form_class=PostForm
    template_name="add_post.html"
    #Show all fields
    #fields="__all__"
    #Show some fields
    #fields=('title','body')
    success_url=reverse_lazy('home')

class UpdatePostView(UpdateView):
    model=Post
    form_class=EditForm
    template_name="update_post.html"
    #fields=['title','title_tag','body']
    success_url=reverse_lazy('home')

class DeletePostView(DeleteView):
    model=Post
    template_name="delete_post.html"
    success_url=reverse_lazy('home')

#Category
class AddCategoryView(CreateView):
    model= Category
    template_name="add_category.html"
    fields='__all__'
    success_url=reverse_lazy('home')

def CategoryView(request,cats):
    #Replace - with " " for categories with multiple words
    category_posts=Post.objects.filter(category__iexact=cats.replace("-"," "))
    return render(request,'categories.html',{'cats':cats.title().replace("-"," "),'category_posts':category_posts})

#Likes and Dislikes
def LikeView(request,pk):
    #Get the id from the button, look it on Post and asign to post variable
    post=get_object_or_404(Post,id=request.POST.get('post_id'))
    #Save the like from an user
    #If the user allready liked a post, unlike is a option
    liked=False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked=False
    else:
        post.likes.add(request.user)
        liked=True
    #Return to the same page instead going home
    #Go to article_details/pk
    return HttpResponseRedirect(reverse('article_details',args=[str(pk)]))

class AddCommentView(CreateView):
    model= Comment
    #Import the PostForm from Forms file
    #Since we use this method, we don't have to show them
    form_class=CommentForm
    template_name="add_comment.html"
    #Show all fields
    #fields="__all__"
    #Show some fields
    #fields=('title','body')
    #success_url=reverse_lazy('home')
    def form_valid(self,form):
        form.instance.post_id=self.kwargs['pk']
        return super().form_valid(form)
    def get_success_url(self):

        return reverse_lazy('article_details', kwargs={'pk': self.kwargs['pk']})

from django.test import TestCase
from django.contrib.auth.models import User
from .models import Category, Post, UserProfile, Comment
from django.urls import reverse

# Create your tests here
class CategoryModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Test Category')

    def test_category_str(self):
        self.assertEqual(str(self.category), 'Test Category')

    def test_category_absolute_url(self):
        #self.assertEqual(self.category.get_absolute_url(), f'')
        self.assertEqual(self.category.get_absolute_url(), reverse('home'))
class PostModelTest(TestCase):
    def setUp(self):
        user = User.objects.create_user(username='testuser', password='testpass')
        self.post = Post.objects.create(
            title='Test Post',
            title_tag='Test Tag',
            author=user,
            body='Test Body',
            category='Test Category',
            post_resume='Test Resume'
        )

    def test_post_absolute_url(self):
        expected_url = reverse("article_details", args=[str(self.post.id)])
        self.assertEqual(self.post.get_absolute_url(), expected_url)

class UserProfileModelTest(TestCase):
    def setUp(self):
        user = User.objects.create_user(username='testuser', password='testpass')
        self.user_profile = UserProfile.objects.create(
            user=user,
            bio='Test Bio',
        )

    def test_user_profile_str(self):
        self.assertEqual(str(self.user_profile), 'testuser')

    def test_user_profile_absolute_url(self):
        self.assertEqual(self.user_profile.get_absolute_url(), '/')

class CommentModelTest(TestCase):
    def setUp(self):
        user = User.objects.create_user(username='testuser', password='testpass')
        post = Post.objects.create(
            title='Test Post',
            title_tag='Test Tag',
            author=user,
            body='Test Body',
            category='Test Category',
            post_resume='Test Resume'
        )
        self.comment = Comment.objects.create(
            post=post,
            name='Test Commenter',
            body='Test Comment Body',
        )

    def test_comment_success_url(self):
        expected_url = reverse('article_details', kwargs={'pk': self.comment.post.pk})
        self.assertEqual(self.comment.get_success_url(), expected_url)
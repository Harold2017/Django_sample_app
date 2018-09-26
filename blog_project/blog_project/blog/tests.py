from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from .models import Post


User = get_user_model()


class BlogTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='test@email.com',
            password='secret'
        )

        self.post = Post.objects.create(
            title='A test title',
            body='A test body',
            author=self.user
        )

    def test_string_representation(self):
        post = Post(title='Another test title')
        self.assertEqual(str(post), post.title)

    def test_post_content(self):
        self.assertEqual(f'{self.post.title}', 'A test title')
        self.assertEqual(f'{self.post.body}', 'A test body')
        self.assertEqual(f'{self.post.author}', 'testuser')

    def test_post_list_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'A test body')
        self.assertTemplateUsed(response, 'home.html')

    def test_post_detail_view(self):
        response = self.client.get('/post/1/')
        no_response = self.client.get('/post/2/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'A test title')
        self.assertTemplateUsed(response, 'post_detail.html')

from django.test import TestCase
from .models import Post
from django.urls import reverse


class BaseTest(TestCase):

    def setUp(self):
        Post.objects.create(text='just a test')


class PostModelTest(BaseTest):

    def test_text_content(self):
        post = Post.objects.first()
        expected_object_name = f'{post.text}'
        self.assertEqual(expected_object_name, 'just a test')


class HomePageViewTest(BaseTest):

    def test_view_url_exists_at_proper_location(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'home.html')

from django.test import TestCase, Client
from datetime import datetime
from django.urls import reverse
from . import models


class EntryTestCase(TestCase):
    def setUp(self):
        models.Entry.objects.create(
            author="Test",
            title="Test Title",
            content="Test Blog Entry",
            date_published=datetime.now(),
            slug="test-title"
        )

    def test_blog_entry_creation(self):
        blog = models.Entry.objects.get(author="Test")
        self.assertTrue(isinstance(blog, models.Entry))
        self.assertEqual(blog.__unicode__(), blog.title)

    def test_blog_list_view(self):
        blog = models.Entry.objects.get(author="Test")
        resp = self.client.get(reverse("blog:blog-home"))

        self.assertEqual(resp.status_code, 200)

    def test_blog_detail_view(self):
        blog = models.Entry.objects.get(author="Test")
        resp = self.client.get(reverse("blog:blog-detail", kwargs={"slug": "test-title"}))

        self.assertEqual(resp.status_code, 200)
        self.assertEqual(blog.title, resp.context['blog'].title)

    def test_blog_create_view(self):
        entry_count = models.Entry.objects.count()
        resp = self.client.post(reverse('blog:blog-new'),
                                {'title': "Test2",
                                 'content': 'More testing',
                                 'author': 'Test Testy',
                                 'slug': 'test2',
                                 'date_published': datetime.now(),
                                 })

        self.assertEqual(resp.status_code, 302)
        self.assertEqual(models.Entry.objects.count(), entry_count+1)

    def test_blog_create_view_invalid(self):
        entry_count = models.Entry.objects.count()
        resp = self.client.post(reverse('blog:blog-new'),
                                {'title': "",
                                 'content': 'More testing',
                                 'author': 'Test Testy',
                                 'slug': 'test2',
                                 'date_published': datetime.now(),
                                 })


        self.assertNotEqual(models.Entry.objects.count(), entry_count + 1)


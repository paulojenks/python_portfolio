from django.test import TestCase, Client
from datetime import datetime
from django.urls import reverse
from . import models


class ProjectTestCase(TestCase):
    def setUp(self):
        models.Project.objects.create(
            name='Test Project',
            description='Test Descriptoin',
            type='Python',
            git_link="www.github.com",
            image='images/about-me.jpg'
        )
        user = models.User.objects.create(username="Test")
        models.Profile.objects.create(
            user = user,
            first_name="Test",
            last_name="Testy",
            username="testy",
            email="test@test.com",
            personal_bio="Testing stuff",
            professional_bio="More testing stuff",
            avatar="images/avatars/44883265_10156868819967171_2977258294361456640_n.jpg"
        )

    def test_project_model(self):
        project = models.Project.objects.get(name="Test Project")
        self.assertTrue(isinstance(project, models.Project))
        self.assertEqual(project.__str__(), project.name)

    def test_project_list_view(self):
        project = models.Project.objects.get(name="Test Project")
        resp = self.client.get(reverse("portfolio:projects"))

        self.assertEqual(resp.status_code, 200)

    def test_project_detail_view(self):
        project = models.Project.objects.get(name="Test Project")
        resp = self.client.get(reverse("portfolio:project", kwargs={"pk": "1"}))

        self.assertEqual(resp.status_code, 200)
        self.assertEqual(project.name, resp.context['project'].name)

    def test_profile_model(self):
        profile = models.Profile.objects.get(first_name="Test")
        self.assertTrue(isinstance(profile, models.Profile))
        self.assertEqual(profile.__str__(), profile.username)

    def test_profile_view(self):
        profile = models.Profile.objects.get(first_name="Test")
        resp = self.client.get(reverse("portfolio:profile", kwargs={'name':profile.first_name}))

        self.assertEqual(resp.status_code, 200)

    def test_home_page(self):
        resp = self.client.get(reverse("portfolio:home"))
        self.assertEqual(resp.status_code, 200)


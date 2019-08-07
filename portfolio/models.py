from django.contrib.auth.models import User
from django.core.validators import EmailValidator
from django.db import models
from django.db.models.signals import post_save


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=50, null=False)
    email = models.EmailField(validators=[EmailValidator])
    first_name = models.CharField(max_length=44)
    last_name = models.CharField(max_length=44)
    personal_bio = models.TextField()
    professional_bio = models.TextField()
    avatar = models.FileField(upload_to="avatars")

    def __str__(self):
        return self.username


def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = Profile.objects.create(user=kwargs['instance'])


post_save.connect(create_profile, sender=User)


class Project(models.Model):
    name = models.CharField(max_length=144, null=False)
    description = models.TextField()
    type = models.CharField(max_length=20)
    git_link = models.URLField()
    image = models.FileField(upload_to='projects', null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name', 'type']

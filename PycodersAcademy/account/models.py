from django.db import models
from django.conf import settings
# Create your models here.


class Courses(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    progress = models.IntegerField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)

    objects = models.Manager()

    def __str__(self):
        return self.name


class RegisteredUser(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    Fullname = models.CharField(max_length=255)
    Email = models.EmailField(max_length=255)

    objects = models.Manager()

    def __str__(self):
        return self.Fullname


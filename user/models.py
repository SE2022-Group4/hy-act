from django.contrib.auth.models import AbstractUser
from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Major(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class User(AbstractUser):
    telephone = models.CharField("telephone number", max_length=150, blank=True)
    departments = models.ManyToManyField(Department, blank=True)
    majors = models.ManyToManyField(Major, blank=True)

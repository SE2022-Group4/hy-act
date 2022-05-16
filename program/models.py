from django.contrib.auth.models import User
from django.db import models


class Program(models.Model):
    manager = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=2000)
    apply_start_at = models.DateTimeField()
    apply_end_at = models.DateTimeField()
    class_start_at = models.DateTimeField()
    class_end_at = models.DateTimeField()


class Application(models.Model):
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField()


class AttendanceCode(models.Model):
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    code = models.CharField(max_length=200)
    created_at = models.DateTimeField()
    expire_at = models.DateTimeField()

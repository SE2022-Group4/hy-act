from django.contrib.auth.models import User
from django.db import models


class ProgramManager(models.Manager):
    def get_queryset(self):
        return super(ProgramManager, self).get_queryset().filter(active=True)


class Program(models.Model):
    manager = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=2000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    apply_start_at = models.DateTimeField()
    apply_end_at = models.DateTimeField()
    program_start_at = models.DateTimeField()
    program_end_at = models.DateTimeField()
    thumbnail_url = models.CharField(max_length=200, null=True)
    location = models.CharField(max_length=200, null=True)
    target_grade = models.CharField(max_length=100, null=True)
    target_major = models.CharField(max_length=100, null=True)
    max_applicant_count = models.IntegerField(default=0)
    active = models.BooleanField(default=True)

    objects = ProgramManager()

    class Meta:
        ordering = ['-created_at']

    def inactivate(self):
        self.active = False


class Application(models.Model):
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField()


class AttendanceCode(models.Model):
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    code = models.CharField(max_length=200)
    created_at = models.DateTimeField()
    expire_at = models.DateTimeField()

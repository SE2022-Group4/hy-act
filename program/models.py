import datetime
import random

from django.contrib.auth import get_user_model
from django.db import models

from user.models import Department

User = get_user_model()

DEFAULT_ATTENDANCE_CODE_LENGTH = 6


def generate_digit_code(length: int = DEFAULT_ATTENDANCE_CODE_LENGTH) -> str:
    format_string = '{0:0' + str(length) + '}'

    return format_string.format(random.randint(0, 10 ** length))


class ProgramManager(models.Manager):
    def get_queryset(self):
        return super(ProgramManager, self).get_queryset().filter(active=True)


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Program(models.Model):
    manager = models.ForeignKey(User, on_delete=models.CASCADE, related_name='managing_program_set')
    lecturer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='instructing_program_set')
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
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True)
    sex = models.SmallIntegerField(null=True)
    max_applicant_count = models.IntegerField(default=0)
    active = models.BooleanField(default=True)

    objects = ProgramManager()

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name

    def inactivate(self):
        self.active = False

    def apply(self, user):
        Application.objects.create(program=self, student=user)

    def recent_applicant_count(self):
        return len(Application.objects.filter(program=self).all())

    def create_attendance_code(self, code_type):
        attendance_code, _ = AttendanceCode.objects.get_or_create(program=self, type=code_type)

        return attendance_code

    def verify_attendance_code(self, code_type, code):
        queryset = AttendanceCode.objects.filter(program=self, type=code_type).all()

        if not queryset.exists():
            return False

        attendance_code = queryset.get()

        return attendance_code.code == code

    def applications(self):
        return self.application_set.all()

    def start_attendance_code(self):
        attendance_code = self.attendancecode_set.filter(type=AttendanceCode.CodeType.START_CODE).first()

        return attendance_code.code if attendance_code is not None else None

    def end_attendance_code(self):
        attendance_code = self.attendancecode_set.filter(type=AttendanceCode.CodeType.END_CODE).first()

        return attendance_code.code if attendance_code is not None else None


class Application(models.Model):
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    attendance_start_at = models.DateTimeField(null=True)
    attendance_end_at = models.DateTimeField(null=True)

    class Meta:
        unique_together = ('program', 'student')

    def start_attendance(self):
        self.attendance_start_at = datetime.datetime.now()
        self.save(update_fields=['attendance_start_at'])

    def end_attendance(self):
        self.attendance_end_at = datetime.datetime.now()
        self.save(update_fields=['attendance_end_at'])


class AttendanceCode(models.Model):
    class CodeType(models.IntegerChoices):
        START_CODE = 0, 'start'
        END_CODE = 1, 'end'

    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    code = models.CharField(max_length=200, default=generate_digit_code)
    type = models.SmallIntegerField(choices=CodeType.choices, default=CodeType.START_CODE)
    created_at = models.DateTimeField(auto_now_add=True)
    expire_at = models.DateTimeField(null=True)

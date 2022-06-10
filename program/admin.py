from django.contrib import admin

# Register your models here.
from program.models import Program, Category

admin.site.register(Program)
admin.site.register(Category)
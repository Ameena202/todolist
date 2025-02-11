from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Task

# Register the Task model to appear in the Django admin interface
admin.site.register(Task)

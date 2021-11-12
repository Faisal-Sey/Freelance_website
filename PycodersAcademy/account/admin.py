from django.contrib import admin
from .models import RegisteredUser, Course
# Register your models here.


admin.site.register(RegisteredUser)
admin.site.register(Course)
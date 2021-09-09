from django.contrib import admin
from .models import RegisteredUser, Courses
# Register your models here.


admin.site.register(RegisteredUser)
admin.site.register(Courses)
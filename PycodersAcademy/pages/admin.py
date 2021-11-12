from django.contrib import admin
from .models import CoursePreview, LearningObjective, CourseDetail, TrainerDetail
# Register your models here.

admin.site.register(CoursePreview)
admin.site.register(LearningObjective)
admin.site.register(CourseDetail)
admin.site.register(TrainerDetail)

from django.contrib import admin
from .models import CoursePreview, LearningObjective, CourseDetails, TrainerDetail
# Register your models here.

admin.site.register(CoursePreview)
admin.site.register(LearningObjective)
admin.site.register(CourseDetails)
admin.site.register(TrainerDetail)

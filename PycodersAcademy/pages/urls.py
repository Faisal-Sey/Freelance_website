from django.urls import path
from . import views
from django.conf import settings
from .views import StudentLesson, CoursePreviewView, LessonView
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home_page, name="home"),
    path('courses', views.courses, name="courses"),
    path('path', views.path, name="path"),
    path('dashboard', views.student_dashboard, name="dashboard"),
    path('my-courses', views.my_courses, name="my_courses"),
    path('course-preview/<slug:slug>/', CoursePreviewView.as_view(), name="course_preview"),
    path('student-lesson/<slug:slug>/', StudentLesson.as_view(), name="student_lesson"),
    path('student-path', views.student_path, name="student_path"),
    path('lesson-view/<slug:slug>', LessonView.as_view(), name="lesson_view")
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
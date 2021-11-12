from django.shortcuts import render
from django.views.generic import View
from .models import CoursePreview, CourseDetail
from django.template.defaulttags import register


def home_page(request):
    return render(request, 'index.html')


def courses(request):
    return render(request, 'course_templates/courses.html')


def path(request):
    return render(request, 'course_templates/paths.html')


def student_dashboard(request):
    return render(request, "accounts/student-dashboard.html")


def my_courses(request):
    return render(request, "accounts/student-my-courses.html")


class StudentLesson(View):
    def get(self, **kwargs):
        slug = kwargs["slug"]
        current_course = CoursePreview.objects.filter(slug=slug)
        context = {'course': current_course}
        return render(self.request, "accounts/student-lesson.html", context)


def student_path(request):
    return render(request, "accounts/student-path.html")


class CoursePreviewView(View):
    def get(self, **kwargs):
        slug = kwargs["slug"]
        current_course = CoursePreview.objects.filter(slug=slug)
        contents = CourseDetail.objects.filter(course_slug=slug).values()
        headers = {}
        status = {}
        videos = {}
        video_length = {}
        templates = {}
        for sect in contents:
            if sect['division_header'] in headers:
                new_details = []
                for details in headers[sect['division_header']]:
                    new_details.append(details)
                new_details.append(sect['description'])
                headers[sect['division_header']] = new_details
            else:
                headers[sect['division_header']] = [sect['description']]
            status[sect['description']] = sect['state']
            videos[sect['description']] = sect['video']
            video_length[sect['description']] = sect['video_length']
            templates[sect['description']] = sect['template_name']
        head_keys = headers.keys()

        @register.filter
        def get_content(dict, key):
            return dict.get(key)

        @register.filter
        def get_slug(dict, key):
            return str(slug) + '-' + str(dict.get(key))

        context = {'course': current_course, 'content_dict': contents, 'head_keys': head_keys,
                   'headers': headers, 'state': status, 'videos': videos, 'video_length': video_length,
                   'template_name': templates}
        return render(self.request, "course_templates/student-course.html", context)


class LessonView(View):
    def get(self, *args, **kwargs):
        slug = kwargs["slug"]
        split_slug = str(slug).split('-')
        template_name = split_slug[1]
        slug_name = split_slug[0]
        # new_slug = CourseDetail.objects.get(slug=slug)
        # new_slug.state = "on"
        # new_slug.save()
        context = {}
        return render(self.request, f"course_templates/{slug_name}/{template_name}.html", context)

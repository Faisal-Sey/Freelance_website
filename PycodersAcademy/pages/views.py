import json
from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View
from django.contrib.auth import authenticate
from .models import CoursePreview, CourseDetails, LearningObjective
from django.template.defaulttags import register
# Create your views here.


def home_page(request):
    return render(request, 'index.html')


def courses(request):
    return render(request, 'courses.html')


def path(request):
    return render(request, 'paths.html')


def student_dashboard(request):
    return render(request, "student-dashboard.html")


def my_courses(request):
    return render(request, "student-my-courses.html")


class StudentLesson(View):
    def get(self, *args, **kwargs):
        slug = kwargs["slug"]
        current_course = CoursePreview.objects.filter(slug=slug)
        context = {'course': current_course}
        return render(self.request, "student-lesson.html", context)


def student_path(request):
    return render(request, "student-path.html")


class CoursePreviewView(View):
    def get(self, *args, **kwargs):
        slug = kwargs["slug"]
        current_course = CoursePreview.objects.filter(slug=slug)
        contents = CourseDetails.objects.filter(course_slug=slug).order_by('time')
        sections = LearningObjective.objects.values()
        content_dict = {}

        for content in contents:
            content_dict[content.course_slug] = content.description



        @register.filter
        def get_contents(dict, key):
            desc = []
            for val in dict:
                if val.division_header == key:
                    desc.append(val.description)
            return desc

        @register.filter
        def check_status(dict, key):
            status_class = CourseDetails.objects.get(description=key)
            status = status_class.state
            return status

        @register.filter
        def reformat_slug(dict, key):
            key_mod = key.split()
            return str(''.join(key_mod))

        @register.filter
        def get_sections(dict, key):
            returning_list = []
            numbers = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five",
                       6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten",
                       11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen",
                       16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen", 20: "twenty"
                       }
            new_dict = dict.filter(slug=key)
            if new_dict:
                for i in range(1, 21):
                    current_1 = numbers[i]
                    if new_dict[0][current_1] is not None:
                        returning_list.append(new_dict[0][current_1])
                    else:
                        break
            return returning_list

        @register.filter
        def check_previous(dict, key):
            details = (CourseDetails.objects.all()).order_by("-time")
            details_list = {}
            for det in details:
                details_list[det.divison_header] = det.state

            state = ""
            key_index = ([details_list.keys()]).index(details_list[key])
            if key_index - 1:
                current_list = ([details_list.keys()])[key_index - 1]
                if details_list[current_list] == "off":
                    print("off")
                    state = "off"
                elif details_list[current_list] == "on":
                    print("on")
                    state = "on"
            else:
                pass

            return state
        context = {'course': current_course, 'content_dict': contents, 'sections': sections}
        return render(self.request, "student-course.html", context)


class LessonView(View):
    def get(self, *args, **kwargs):
        slug = kwargs["slug"]
        new_slug = CourseDetails.objects.get(slug=slug)
        new_slug.state = "on"
        new_slug.save()
        context = {'header': new_slug.description}
        return render(self.request, "lesson-view.html", context)
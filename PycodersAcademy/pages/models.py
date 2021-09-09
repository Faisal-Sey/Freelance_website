from django.db import models

# Create your models here.
class CoursePreview(models.Model):
    course_name = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    logo = models.ImageField()
    trainer = models.CharField(max_length=500)
    trainer_image = models.ImageField()
    header = models.CharField(max_length=255)
    description = models.TextField()
    video_time = models.CharField(max_length=50, blank=True, null=True)
    video = models.FileField(blank=True, null=True)
    ratings = models.CharField(max_length=50, blank=True, null=True)
    slug = models.CharField(max_length=50)
    section_1 = models.CharField(max_length=150, blank=True, null=True)
    about_course = models.CharField(max_length=500, blank=True, null=True)
    about_trainer = models.CharField(max_length=500, blank=True, null=True)

    objects = models.Manager()

    def __str__(self):
        return self.course_name


class LearningObjective(models.Model):
    slug = models.CharField(max_length=50)
    one = models.CharField(max_length=255, blank=True, null=True)
    two = models.CharField(max_length=255, blank=True, null=True)
    three = models.CharField(max_length=255, blank=True, null=True)
    four = models.CharField(max_length=255, blank=True, null=True)
    five = models.CharField(max_length=255, blank=True, null=True)
    six = models.CharField(max_length=255, blank=True, null=True)
    seven = models.CharField(max_length=255, blank=True, null=True)
    eight = models.CharField(max_length=255, blank=True, null=True)
    nine = models.CharField(max_length=255, blank=True, null=True)
    ten = models.CharField(max_length=255, blank=True, null=True)
    eleven = models.CharField(max_length=255, blank=True, null=True)
    twelve = models.CharField(max_length=255, blank=True, null=True)
    thirteen = models.CharField(max_length=255, blank=True, null=True)
    fourteen = models.CharField(max_length=255, blank=True, null=True)
    fifteen = models.CharField(max_length=255, blank=True, null=True)
    sixteen = models.CharField(max_length=255, blank=True, null=True)
    seventeen = models.CharField(max_length=255, blank=True, null=True)
    eighteen = models.CharField(max_length=255, blank=True, null=True)
    nineteen = models.CharField(max_length=255, blank=True, null=True)
    twenty = models.CharField(max_length=255, blank=True, null=True)
    objects = models.Manager()

    def __str__(self):
        return self.slug


class TrainerDetail(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    slug = models.CharField(unique=True, max_length=50)

    objects = models.Manager()

    def __str__(self):
        return self.name


class CourseDetails(models.Model):
    slug = models.CharField(max_length=50)
    division_header = models.CharField(max_length=255)
    description = models.TextField(max_length=500)
    video_length = models.CharField(max_length=10, blank=True, null=True)
    video = models.FileField(blank=True, null=True)
    course_slug = models.CharField(max_length=50)
    state = models.CharField(max_length=20)
    time = models.DateTimeField(auto_now_add=True)

    objects = models.Manager()

    def __str__(self):
        return self.slug
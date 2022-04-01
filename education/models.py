from django.db import models
from django.db.models.fields.related import ManyToManyField
from django.utils import timezone

# Create your models here.

def topic_directory_path(instance, filename):
    return 'education/{0}/{1}/{2}'.format(instance.subject, instance.title, filename)

def lesson_directory_path(instance, filename):
    return 'education/{0}/{1}/lesson #{2}/{3}/{4}'.format(instance.subject, instance.topic, instance.lesson_number, instance.title, filename)



class Organization(models.Model):
    name = models.CharField(max_length=20, primary_key=True)

    def __str__(self):
        return self.name


class Human(models.Model):
    id = models.CharField(max_length=7, primary_key=True, default='GR-ORG')
    first_name = models.CharField(max_length=20, null=True)
    last_name = models.CharField(max_length=20)
    organization = models.ForeignKey(Organization, on_delete= models.CASCADE, null=True)

    def completeName(self):
        txt = "{0} {1}"
        return txt.format(self.first_name, self.last_name)

    def __str__(self):
        return self.completeName()


class Subject(models.Model):
    subject = models.CharField(max_length=20, primary_key=True)

    def __str__(self):
        return self.subject

# Tech! 
class Topic(models.Model):
    id = models.CharField(max_length=255, primary_key=True, default='slug')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, blank=True, null=True)
    humans = ManyToManyField(Human)
    title = models.CharField(max_length=20)
    subtitle = models.CharField(max_length=100, null=True)
    level = models.IntegerField(blank=True, null=True)
    thumbnail = models.ImageField(upload_to=topic_directory_path, blank=True, null=True)
    slug = models.SlugField(max_length=250, unique_for_date='start', null=False, unique=True)
    start = models.DateTimeField(default=timezone.now)
    is_complete = models.BooleanField(default=False)

    class Meta:
        ordering = ('-start',)
    
    def __str__(self):
        return self.title

# Ideas! | Explication!
class Lesson(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Out of Education', 'Out of Education'),
        ('Completed', 'Completed'),
        ) 
    id = models.CharField(max_length=255, primary_key=True, default='slug')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, blank=True, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, blank=True, null=True)
    lesson_number = models.IntegerField(blank=True, null=True)
    title = models.CharField(max_length=20)
    subtitle = models.CharField(max_length=100, null=True)
    description = models.TextField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    level = models.IntegerField(blank=True, null=True)
    thumbnail = models.ImageField(upload_to=lesson_directory_path, blank=True, null=True)
    status = models.CharField(max_length=20, null=True, choices=STATUS)
    slug = models.SlugField(max_length=250, null=False, unique=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ('-lesson_number',)
    
    def __str__(self):
        return self.title
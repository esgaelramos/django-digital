from django.contrib import admin

from .models import Human, Organization, Subject, Topic, Lesson

admin.site.register(Human)
admin.site.register(Organization)
admin.site.register(Subject)
admin.site.register(Topic)
admin.site.register(Lesson)
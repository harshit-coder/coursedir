
from django.contrib import admin
from django.contrib.auth.models import User, Group

from .models import *
# Register your models here.
admin.site.unregister(User)
admin.site.unregister(Group)

admin.site.register(quiz)


class answerinlinemodel(admin.TabularInline):
    model = Answer


class questionmodeladmin(admin.ModelAdmin):
    inlines = [answerinlinemodel]


admin.site.register(Question, questionmodeladmin)

admin.site.register(course)

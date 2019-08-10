from django.contrib import admin
from .models import master_courses, course_category, courses_series
from tinymce.widgets import TinyMCE
from django.db import models
# from tinymce.widgets import TinyMCE


# Register your models here.
class master_coursesAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Titles/Duration/Image", {"fields": ["course_title", "course_duration"]}),
        ("URL", {"fields": ["course_slug"]}),
        ("Series", {"fields": ["course_series"]}),
        ("Contents", {"fields": ["course_contents"]}),
    ]


    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()}
    }
admin.site.register(courses_series)    
admin.site.register(course_category)
admin.site.register(master_courses, master_coursesAdmin)


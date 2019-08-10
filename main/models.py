from django.db import models

# Create your models here.
class course_category(models.Model):
    course_category = models.CharField(max_length=200)
    course_summary = models.CharField(max_length=200)
    course_slug = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "Course Categories"
    
    def __str__(self):
        return self.course_category



class courses_series(models.Model): #make this courses_series
    course_series = models.CharField(max_length=200)
    course_category = models.ForeignKey(course_category, default=1, verbose_name="Category", on_delete=models.SET_DEFAULT)
    series_summary = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "Course Series"

    def __str__(self):
        return self.course_series



class master_courses(models.Model):
    course_title = models.CharField(max_length=200)
    course_duration = models.IntegerField(default=1)
    course_contents = models.TextField(default=1)
    course_series = models.ForeignKey(courses_series, default=1, verbose_name="Series", on_delete=models.SET_DEFAULT)
    course_slug = models.CharField(max_length=200, default=1)
    date_added = models.DateTimeField("Date Published", auto_now_add=True)
    

    def __str__(self):
        return self.course_title

    class Meta:
        verbose_name_plural = "Courses"

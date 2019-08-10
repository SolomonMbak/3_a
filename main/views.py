from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import master_courses, course_category, courses_series
from django.contrib import messages
from django.contrib.auth.decorators import login_required



# from main.forms import PasswordChangeForm
@login_required(login_url='/accounts/login/')
def single_slug(request, single_slug):
    categories = [c.course_slug for c in course_category.objects.all()]
    if single_slug in categories:
        matching_series = courses_series.objects.filter(course_category__course_slug=single_slug)

        series_urls = {}
        for ms in matching_series.all():
            part_one = master_courses.objects.filter(course_series__course_series=ms.course_series).earliest("date_added")
            series_urls[ms] = part_one.course_slug
            
        return render(request, "main/category.html", {"the_series": series_urls})

    masterCourses = [m.course_slug for m in master_courses.objects.all()]
    if single_slug in masterCourses:
        this_course = master_courses.objects.get(course_slug = single_slug)

        # Getting the series
        course_from_series = master_courses.objects.filter(course_series__course_series=this_course.course_series).order_by("date_added")

        # fetch the indexes of the courses
        this_course_index = list(course_from_series).index(this_course)

        return render(request, "main/course.html", {"the_course": this_course,
                                                    "sidebar": course_from_series,
                                                    "this_course_idx": this_course_index})


    return HttpResponse("{single_slug} doesnt exist at all.")


def index(request):
    return render(request=request, template_name='main/course_cat.html', context={"course_cat": course_category.objects.all})


def about(request):
    return render(request, "main/about.html")


def privacy_policy(request):
    return render(request, "main/privacy_policy.html")


def terms(request):
    return render(request, "main/terms.html")


def publish_a_course(request):
    return render(request, "main/publish_a_course.html")

"""
course query system views
"""
from django.shortcuts import render
from django.http import HttpResponse
from querysys.models import Course, Teacher, Department, ClassTime
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import datetime


def index(request):
    """
    return the main page
    """

    return render(request, 'index.html', locals())


def result(request):
    """
    return the result
    """
    courses = Course.objects.all()

    paginator = Paginator(courses, 2)
    page = request.GET.get('page')

    try:
        courses = paginator.page(page)
    except PageNotAnInteger:
        courses = paginator.page(1)
    except EmptyPage:
        courses = paginator.page(paginator.num_pages)

    return render(request, 'result.html', {'courses': courses})


def set_class_time(request):
    """
    Configure all ClassTime
    """
    for day in range(1, 8):
        for sect in range(1, 17):
            if not ClassTime.objects.filter(section=sect, day=day):
                ClassTime.objects.create(
                    section=sect,
                    day=day,
                    start_time=datetime.time(hour=5+sect, minute=10),
                    end_time=datetime.time(hour=6+sect)
                )
            else:
                return HttpResponse('Maybe you have created ClassTime data.')
    return HttpResponse("Configure ClassTime Successfully.")


def import_data_from_csv(request):
    """
    import course data form csv
    """

    return HttpResponse("Import Data Successfully.")

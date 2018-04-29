"""
course query system views
"""
from django.shortcuts import render
from django.http import HttpResponse
from querysys.models import Course, Teacher, Department, ClassTime


def result(request):
    """
    return the result
    """
    courses = Course.objects.all()
    return render(request, 'result.html', {'courses': courses})


def setClassTime(request):
    """
    Configure all ClassTime
    """
    # type something
    return HttpResponse("Configure ClassTime Successfully.")

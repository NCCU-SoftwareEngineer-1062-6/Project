"""
course query system views
"""
from django.shortcuts import render
from querysys.models import Course, Teacher, Department, ClassTime


def result(request):
    """
    return the result
    """
    courses = Course.objects.all()
    return render(request, 'result.html', {'courses': courses})

"""
course query system views
"""
from django.shortcuts import render
from django.http import HttpResponse
from querysys.models import Course, Teacher, Department, ClassTime
import datetime
from django.shortcuts import render_to_response

#test
from querysys.models import user
from .filters import UserFilter, CourseFilter

def search(request):
    user_list = user.objects.all()
    user_filter = UserFilter(request.GET, queryset=user_list)
    return render(request, 'user_list.html', {'filter': user_filter})

def search2(request):

    request.encoding='utf-8'
    courses = Course.objects.filter(name_zh = 'no class' )
    courses_teacher_output = Course.objects.filter(name_zh = 'no class' )
    if 'q' in request.GET:
        #chain class name , teacher
        teacher1 = Teacher.objects.filter(name_zh__contains=request.GET['q'])
        courses_name_output = Course.objects.filter(name_zh__contains = request.GET['q'] )
        if teacher1.count() > 0 :
            #courses_teacher_output = Course.objects.filter(teacher__contains= teacher1[0].id )
            courses_teacher_output = Course.objects.filter(teacher__name_zh__contains = request.GET['q'] )
            courses = courses_teacher_output|courses_name_output
        else:
            courses = courses_name_output

        #chain location
        location_output = Course.objects.filter(location__contains = request.GET['q'] )
        courses = courses|location_output

        #chain department
        department_output = Course.objects.filter(department__name_zh__contains = request.GET['q'] )
        courses = courses|department_output

        #chain token
        try:
            token_output = Course.objects.filter(token = request.GET['q'] )
            courses = courses|token_output
        except:
            courses = courses

    course_list = courses
    course_filter = CourseFilter(request.GET, queryset=course_list)
    return render(request, 'course_list.html', {'filter': course_filter})
#test

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

# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.shortcuts import render
from querysys.models import Course, Teacher, Department, ClassTime
from itertools import chain
from decimal import Decimal


#屬性名+__contains=值

# 表单
def search_form(request):
    return render_to_response('search_form.html')


def search(request):
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
        #token_output = Course.objects.filter(token = request.GET['q'] )
        #courses = chain(courses, token_output)

    return render(request, 'result.html', {'courses': courses})

#搜尋老師
#部份匹配
def search_teacher(request):
    request.encoding='utf-8'
    courses = Course.objects.filter(name_zh = 'no class' )
    courses_teacher_output = Course.objects.filter(name_zh = 'no class' )
    if 'q' in request.GET:
        teacher1 = Teacher.objects.filter(name_zh__contains=request.GET['q'])
        if teacher1.count() > 0 :
            courses_teacher_output = Course.objects.filter(teacher__contains= teacher1[0].id )

        courses = courses_teacher_output

    return render(request, 'result.html', {'courses': courses})

#搜尋課名
#部份匹配
def search_courses(request):
    request.encoding='utf-8'
    courses = Course.objects.filter(name_zh = 'no class' )
    if 'q' in request.GET:
        courses_name_output = Course.objects.filter(name_zh__contains = request.GET['q'] )
        courses = courses_name_output

    return render(request, 'result.html', {'courses': courses})

#搜尋課程代號
#全對才匹配
def search_token(request):
    request.encoding='utf-8'
    #courses = Course.objects.filter(token = 'no class' )
    if 'q' in request.GET:
        token_output = Course.objects.filter(token = request.GET['q'] )
        courses = token_output

    return render(request, 'result.html', {'courses': courses})


#搜尋上課地點
#部份匹配
def search_location(request):
    request.encoding='utf-8'
    if 'q' in request.GET:
        location_output = Course.objects.filter(location__contains = request.GET['q'] )
        courses = location_output

    return render(request, 'result.html', {'courses': courses})

def search_department(request):
    request.encoding='utf-8'
    if 'q' in request.GET:
        department_output = Course.objects.filter(department__name_zh__contains = request.GET['q'] )
        courses = department_output

    return render(request, 'result.html', {'courses': courses})

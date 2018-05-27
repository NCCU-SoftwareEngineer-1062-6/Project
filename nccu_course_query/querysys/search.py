# -*- coding: utf-8 -*-
 
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.shortcuts import render
from querysys.models import Course, Teacher, Department, ClassTime
from itertools import chain
 

#屬性名+__contains=值

# 表单
def search_form(request):
    return render_to_response('search_form.html')
 
# 接收请求数据
def search(request):  
    request.encoding='utf-8'
    courses = Course.objects.filter(name_zh = 'no class' )
    courses_teacher_output = Course.objects.filter(name_zh = 'no class' )
    if 'q' in request.GET:
        #message = '你搜索的内容为: ' + request.GET['q']
        teacher1 = Teacher.objects.filter(name_zh=request.GET['q'])
        if teacher1.count() > 0 :
            courses_teacher_output = Course.objects.filter(teacher= teacher1[0].id )
            
        courses_name_output = Course.objects.filter(name_zh = request.GET['q'] )
        courses = chain( courses_teacher_output ,courses_name_output)

    #return HttpResponse(message)
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
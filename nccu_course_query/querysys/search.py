# -*- coding: utf-8 -*-
 
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.shortcuts import render
from querysys.models import Course, Teacher, Department, ClassTime
from itertools import chain
 
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
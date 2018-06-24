"""
course query system views
"""
import datetime
import json
from querysys import search
from django.shortcuts import render
from django.http import HttpResponse
from querysys.models import Course, Teacher, Department, ClassTime
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .form import textForm


def index(request):
    """
    return the main page
    """
    if request.method == 'POST':  # 当提交表单时

        form = textForm(request.POST)  # form 包含提交的数据

        if form.is_valid():  # 如果提交的数据合法
            searchText = form.cleaned_data['searchText']
            results = search.tokenSearch(searchText)
            results = search.TeacherSearch(searchText) | results
            results = search.zhNameSearch(searchText) | results
            results = search.DepartmentSearch(searchText) | results
            results.distinct()

            return result(request, courses=results)

    else:  # 当正常访问时
        form = textForm()
    return render(request, 'index.html', {'form': form})


def result(request, courses=None):
    """
    return the result
    """
    if courses is None:
        courses = Course.objects.all()

    paginator = Paginator(courses, 10)
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


def import_data_from_json(request):
    """
    import course data form json
    匯入位於同目錄底下的json檔 進 資料庫

    """
    def transform(text):
        if text[0] == '必':
            return 'RE'
        elif text[0] == '選':
            return 'ELE'
        elif text[0] == '群':
            return 'PART'
        return None

    def trans_week(text):
        tmp = None
        if text[0] == '一':
            tmp = 1
        elif text[0] == '二':
            tmp = 2
        elif text[0] == '三':
            tmp = 3
        elif text[0] == '四':
            tmp = 4
        elif text[0] == '五':
            tmp = 5
        elif text[0] == '六':
            tmp = 6
        elif text[0] == '日':
            tmp = 7
        return tmp

    def trans_section(text):
        tmp = None
        if text[0] == 'A':
            tmp = 1
        elif text[0] == 'B':
            tmp = 2
        elif text[0] == '1':
            tmp = 3
        elif text[0] == '2':
            tmp = 4
        elif text[0] == '3':
            tmp = 5
        elif text[0] == '4':
            tmp = 6
        elif text[0] == 'C':
            tmp = 7
        elif text[0] == 'D':
            tmp = 8
        elif text[0] == '5':
            tmp = 9
        elif text[0] == '6':
            tmp = 10
        elif text[0] == '7':
            tmp = 11
        elif text[0] == '8':
            tmp = 12
        elif text[0] == 'E':
            tmp = 13
        elif text[0] == 'F':
            tmp = 14
        elif text[0] == 'G':
            tmp = 15
        elif text[0] == 'H':
            tmp = 16

        return tmp

    with open("querysys/1061-course-result.json", encoding='utf-8', mode='r') as file:
        datas = json.load(file)
        for data in datas:
            c = Course.objects.create(
                token=data['課程代號'],
                credit=int(float(data['學分數'])),
                name_zh=data['課程名稱'],
                name_eng=data['CourseName'],
                category=transform(data['修別']),
                description=data['課程簡介']
            )

            for d in data['開課單位']:
                tmp_department = Department.objects.filter(name_zh=d)
                if not tmp_department.exists():
                    tmp_department = Department.objects.create(
                        name_zh=d
                    )
                    c.department.add(tmp_department)
                else:
                    c.department.add(tmp_department[0])

            for t in data['授課老師']:
                tmp_teacher = Teacher.objects.filter(name_zh=t)
                if not tmp_teacher.exists():
                    tmp_teacher = Teacher.objects.create(
                        name_zh=t
                    )
                    c.teacher.add(tmp_teacher)
                else:
                    c.teacher.add(tmp_teacher[0])

            if data['上課時間'] is not None:
                for time in data['上課時間']:
                    tmp_time = ClassTime.objects.get(
                        day=trans_week(time['day']),
                        section=trans_section(time['section'])
                    )
                    c.course_time.add(tmp_time)

    return HttpResponse("Import datas Successfully.")

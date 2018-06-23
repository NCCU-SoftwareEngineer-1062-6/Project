"""
course query system views
"""
import datetime
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

            return result(request, courses=results)

    else:  # 当正常访问时
        form = textForm()
    return render(request, 'index.html', {'form': form})


def result(request, courses=None):
    """
    return the result
    """
    if courses == None:
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
    import course data form csv
    """

    return HttpResponse("Import Data Successfully.")

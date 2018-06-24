"""
搜尋函式們
"""
from querysys.models import Course

"""
 分別實作搜索以下內容
 科目代號、科目中文、任課教師、上課時間、開課單位
 回傳符合的 course query-set
"""


def tokenSearch(text):
    text = str(text)
    results = Course.objects.filter(token__icontains=text)
    return results


def zhNameSearch(text):
    text = str(text)
    results = Course.objects.filter(name_zh__icontains=text)
    return results


def TeacherSearch(text):
    text = str(text)
    results = Course.objects.filter(teacher__name_zh__icontains=text)
    return results


def DepartmentSearch(text):
    text = str(text)
    results = Course.objects.filter(department__name_zh__icontains=text)
    return results


def CourseTimeSearch():
    return Course.objects.none()

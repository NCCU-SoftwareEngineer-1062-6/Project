from django import forms
from querysys.models import user, Course, Department, ClassTime, Teacher
import django_filters

class UserFilter(django_filters.FilterSet):
    first_name = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = user
        fields = ['username', 'first_name', 'last_name', ]

class CourseFilter(django_filters.FilterSet):
    name_zh = django_filters.CharFilter(lookup_expr='icontains')
    location = django_filters.CharFilter(lookup_expr='icontains')
    department = django_filters.ModelMultipleChoiceFilter(queryset=Department.objects.all(), widget=forms.CheckboxSelectMultiple)
    teacher = django_filters.ModelMultipleChoiceFilter(queryset=Teacher.objects.all(), widget=forms.CheckboxSelectMultiple)
    course_time = django_filters.ModelMultipleChoiceFilter(queryset=ClassTime.objects.all(), widget=forms.CheckboxSelectMultiple)
    class Meta:
        model = Course
        fields = ['token', 'name_zh', 'location', 'department', 'teacher', 'course_time' ]

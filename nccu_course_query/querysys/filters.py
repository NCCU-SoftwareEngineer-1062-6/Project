from django import forms
from querysys.models import user, Course, Department
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
    class Meta:
        model = Course
        fields = ['token', 'name_zh', 'location', 'department' ]

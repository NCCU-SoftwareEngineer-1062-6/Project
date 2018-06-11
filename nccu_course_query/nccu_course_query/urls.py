"""nccu_course_query URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from querysys import views
from querysys import search, search2

#test
from django_filters.views import FilterView
from querysys.filters import UserFilter


urlpatterns = [

    #re_path(r'^search/$', views.search, name='search'),
    re_path(r'^search/$', FilterView.as_view(filterset_class=UserFilter,template_name='user_list.html'), name='search'),

    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('result/', views.result, name='result'),
    path('setup/', views.set_class_time, name='setup'),
    re_path(r'^search-form$', search.search_form),
    #re_path(r'^search$', search.search),
    re_path(r'^search_teacher$', search.search_teacher),
    re_path(r'^search_courses$', search.search_courses),
    re_path(r'^search_token$', search.search_token),
    re_path(r'^search_location$', search.search_location),
    re_path(r'^search_department$', search.search_department),
    re_path(r'^search-post$', search2.search_post),

]

from django.contrib import admin
from .models import Course, Teacher, Language, Location, Class_time
# Register your models here.

admin.site.register(Course)
admin.site.register(Teacher)
admin.site.register(Language)
admin.site.register(Location)
admin.site.register(Class_time)

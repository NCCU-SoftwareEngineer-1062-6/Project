from django.contrib import admin
from .models import Course, Teacher, ClassTime, Department, CollegeProgram, user
# Register your models here.

admin.site.register(Course)
admin.site.register(Department)
admin.site.register(Teacher)
admin.site.register(ClassTime)
admin.site.register(CollegeProgram)

admin.site.register(user)

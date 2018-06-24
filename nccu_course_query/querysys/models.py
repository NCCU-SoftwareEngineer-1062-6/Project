"""
querysys models
"""
from django.db import models


class Course(models.Model):
    """
    the main model of course
    """
    token = models.CharField(max_length=8, primary_key=True)  # 課程代號
    credit = models.SmallIntegerField()  # 學分數
    name_zh = models.CharField(max_length=50)  # 課名 中文
    name_eng = models.CharField(max_length=100)  # 課名 英文
    category = models.CharField(max_length=1)  # 選修 必修 群修
    description = models.TextField()  # 課程簡介

    # many to many field
    department = models.ManyToManyField('Department')  # 開課單位

    teacher = models.ManyToManyField('Teacher')
    """
    it will have more than one teacher in a course.
    And,teacher could teach more than one course.
    """

    course_time = models.ManyToManyField('ClassTime')
    """
    it will have more than one time period in a course.
    And,every time period would have more than one course.
    """

    def __str__(self):
        # name of course
        return self.name_zh


class Teacher(models.Model):
    """
    model teacher
    """
    id = models.AutoField(primary_key=True)
    name_zh = models.CharField(max_length=50)

    def __str__(self):
        return self.name_zh


class Department(models.Model):
    """
    model department which establishs the course.
    """
    id = models.AutoField(primary_key=True)
    name_zh = models.CharField(max_length=50)

    def __str__(self):
        return self.name_zh


class ClassTime(models.Model):
    """
    it have 16 period per day,and 7 days per week.
    """
    id = models.AutoField(primary_key=True)
    section = models.CharField(blank=True,max_length=1)  # 節數 max = 16 , min=1
    day = models.CharField(blank=True,max_length=1)  # 星期幾  用數字表示
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        # name of ClassTime , like "星期7 5節"
        return "星期" + str(self.day) + " " + str(self.section) + "節"

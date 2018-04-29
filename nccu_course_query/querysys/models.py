"""
querysys models
"""
from django.db import models
from django.utils import timezone


class Course(models.Model):
    """
    the main model of course
    """
    token = models.DecimalField(
        max_digits=8, decimal_places=0, primary_key=True)  # 課程代號
    credit = models.SmallIntegerField()  # 學分數
    name_zh = models.CharField(max_length=50)  # 課名 中文
    name_eng = models.CharField(max_length=100)  # 課名 英文
    location = models.CharField(max_length=100)  # 上課地點
    CATEGORY = (
        ('RE', 'Required 必修'),
        ('ELE', 'Elective 選修'),
        ('PART', 'Partially 群修')
    )
    category = models.CharField(choices=CATEGORY, max_length=10)  # 選修 必修 群修
    language = models.CharField(max_length=50)  # 上課語言
    is_core_general_Course = models.BooleanField()  # 是否為核心通識
    change_note = models.TextField()  # 異動資訊
    note = models.TextField()  # 備註

    # FK
    department = models.ForeignKey(
        'Department', on_delete=models.CASCADE)  # 開課單位

    # many to many field
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
    name_eng = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name_zh


class Department(models.Model):
    """
    model department which establishs the course.
    """
    id = models.AutoField(primary_key=True)
    name_zh = models.CharField(max_length=50)
    name_eng = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name_zh


class ClassTime(models.Model):
    """
    it have 16 period per day,and 7 days per week.
    """
    id = models.AutoField(primary_key=True)
    section = models.SmallIntegerField()  # 節數 max = 16 , min=1
    day = models.SmallIntegerField()  # 星期幾  用數字表示
    start_time = models.TimeField()
    end_time = models.TimeField()

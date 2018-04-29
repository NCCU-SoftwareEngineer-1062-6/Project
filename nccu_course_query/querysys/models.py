from django.db import models
from django.utils import timezone

# Create your models here.


class Course(models.Model):
    token = models.IntegerField(max_length=9, primary_key=True)  # 課程代號
    credit = models.SmallIntegerField(max_length=1)  # 學分數
    name_zh = models.CharField(max_length=50)  # 課名 中文
    name_eng = models.CharField(max_length=100)  # 課名 英文
    teacher = models.ForeignKey(
        'Teacher', on_delete=models.CASCADE)  # 教師名 會有多個教師同教
    department = models.ForeignKey(
        'Department', on_delete=models.CASCADE)  # 開課單位
    class_time = models.ForeignKey(
        'Class_time', on_delete=models.CASCADE)  # 上課時間 mutilvalue
    location = models.ForeignKey('Location', on_delete=models.CASCADE)  # 上課地點
    CATEGORY = (
        ('RE', 'Required 必修'),
        ('ELE', 'Elective 選修'),
        ('PART', 'Partially 群修')
    )
    category = models.CharField(choices=CATEGORY)  # 選修 必修 群修
    language = models.ForeignKey('Language', on_delete=models.CASCADE)  # 上課語言
    is_core_general_Course = models.BooleanField()  # 是否為核心通識
    change_note = models.TextField()  # 異動資訊
    note = models.TextField()  # 備註


class Language(models.Model):
    name_zh = models.CharField(max_length=10)
    name_eng = models.CharField(max_length=20)


class Teacher(models.Model):
    name_zh = models.CharField(max_length=50)
    name_eng = models.CharField(max_length=100)


class Department(models.Model):
    name_zh = models.CharField(max_length=50)
    name_eng = models.CharField(max_length=100)


class Class_time(models.Model):
    token = models.IntegerField()
    start_time = models.TimeField()
    end_time = models.TimeField()


class Location(models.Model):
    name_zh = models.CharField(max_length=50)
    name_eng = models.CharField(max_length=100)
    token = models.IntegerField(null=True)

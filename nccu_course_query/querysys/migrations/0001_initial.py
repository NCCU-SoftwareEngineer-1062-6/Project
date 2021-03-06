# Generated by Django 2.0.4 on 2018-04-29 13:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClassTime',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('token', models.IntegerField(max_length=9, primary_key=True, serialize=False)),
                ('credit', models.SmallIntegerField(max_length=1)),
                ('name_zh', models.CharField(max_length=50)),
                ('name_eng', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('category', models.CharField(choices=[('RE', 'Required 必修'), ('ELE', 'Elective 選修'), ('PART', 'Partially 群修')], max_length=10)),
                ('language', models.CharField(max_length=50)),
                ('is_core_general_Course', models.BooleanField()),
                ('change_note', models.TextField()),
                ('note', models.TextField()),
                ('course_time', models.ManyToManyField(to='querysys.ClassTime')),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name_zh', models.CharField(max_length=50)),
                ('name_eng', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name_zh', models.CharField(max_length=50)),
                ('name_eng', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='querysys.Department'),
        ),
        migrations.AddField(
            model_name='course',
            name='teacher',
            field=models.ManyToManyField(to='querysys.Teacher'),
        ),
    ]

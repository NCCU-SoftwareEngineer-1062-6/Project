# Generated by Django 2.0.4 on 2018-06-24 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('querysys', '0006_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='user',
        ),
        migrations.RemoveField(
            model_name='course',
            name='change_note',
        ),
        migrations.RemoveField(
            model_name='course',
            name='is_core_general_Course',
        ),
        migrations.RemoveField(
            model_name='course',
            name='language',
        ),
        migrations.RemoveField(
            model_name='course',
            name='location',
        ),
        migrations.RemoveField(
            model_name='course',
            name='note',
        ),
        migrations.RemoveField(
            model_name='department',
            name='college_program',
        ),
        migrations.AddField(
            model_name='course',
            name='description',
            field=models.TextField(default='test'),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='course',
            name='department',
        ),
        migrations.AddField(
            model_name='course',
            name='department',
            field=models.ManyToManyField(to='querysys.Department'),
        ),
        migrations.DeleteModel(
            name='CollegeProgram',
        ),
    ]
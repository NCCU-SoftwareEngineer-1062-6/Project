# Generated by Django 2.0.4 on 2018-04-30 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('querysys', '0003_auto_20180430_1030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collegeprogram',
            name='name_eng',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='department',
            name='name_eng',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='name_eng',
            field=models.CharField(max_length=100, null=True),
        ),
    ]

# Generated by Django 2.0.4 on 2018-06-24 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('querysys', '0008_auto_20180624_1516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classtime',
            name='day',
            field=models.CharField(blank=True, max_length=1),
        ),
        migrations.AlterField(
            model_name='classtime',
            name='section',
            field=models.CharField(blank=True, max_length=1),
        ),
        migrations.AlterField(
            model_name='course',
            name='category',
            field=models.CharField(max_length=1),
        ),
    ]

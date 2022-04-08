# Generated by Django 3.2.11 on 2022-04-08 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contest', '0011_auto_20220408_2245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contest',
            name='duration',
            field=models.IntegerField(null=True, verbose_name='时长'),
        ),
        migrations.AlterField(
            model_name='grade',
            name='contest',
            field=models.ManyToManyField(to='contest.Contest'),
        ),
    ]

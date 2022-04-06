# Generated by Django 3.2.11 on 2022-04-06 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contest', '0009_auto_20220406_1213'),
    ]

    operations = [
        migrations.AddField(
            model_name='contest',
            name='endtime',
            field=models.DateTimeField(blank=True, null=True, verbose_name='结束时间'),
        ),
        migrations.AlterField(
            model_name='contest',
            name='starttime',
            field=models.DateTimeField(blank=True, null=True, verbose_name='开始时间'),
        ),
        migrations.AlterField(
            model_name='grade',
            name='contest',
            field=models.ManyToManyField(to='contest.Contest'),
        ),
    ]

# Generated by Django 3.2.11 on 2022-03-06 11:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contest', '0002_auto_20220306_1954'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='question',
            new_name='question_message',
        ),
    ]

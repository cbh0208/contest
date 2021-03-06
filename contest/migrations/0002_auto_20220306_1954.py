# Generated by Django 3.2.11 on 2022-03-06 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contest', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='optionA',
            new_name='option_A',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='optionB',
            new_name='option_B',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='optionC',
            new_name='option_C',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='optionD',
            new_name='option_D',
        ),
        migrations.AddField(
            model_name='question',
            name='type',
            field=models.CharField(choices=[('SC', 'single choice'), ('MC', 'multiple choice'), ('JQ', 'judgement'), ('EQ', 'essay')], default='SC', max_length=2),
        ),
    ]

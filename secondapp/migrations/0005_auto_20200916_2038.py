# Generated by Django 3.1 on 2020-09-16 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secondapp', '0004_remove_question_qtitle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partquestion',
            name='partdesc',
            field=models.CharField(max_length=1500),
        ),
    ]

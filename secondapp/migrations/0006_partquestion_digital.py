# Generated by Django 3.1 on 2020-09-20 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secondapp', '0005_auto_20200916_2038'),
    ]

    operations = [
        migrations.AddField(
            model_name='partquestion',
            name='digital',
            field=models.BooleanField(default=False),
        ),
    ]

# Generated by Django 3.1 on 2020-09-16 14:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('secondapp', '0002_partquestion'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='partquestion_id',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='secondapp.partquestion'),
            preserve_default=False,
        ),
    ]

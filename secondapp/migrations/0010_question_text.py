# Generated by Django 3.1 on 2020-09-20 14:03

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('secondapp', '0009_auto_20200920_1220'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='text',
            field=ckeditor_uploader.fields.RichTextUploadingField(default=2),
            preserve_default=False,
        ),
    ]
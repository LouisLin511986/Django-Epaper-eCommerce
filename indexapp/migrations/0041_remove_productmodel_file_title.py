# Generated by Django 4.1.1 on 2022-10-16 07:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('indexapp', '0040_delete_document_productmodel_datetimeofupload_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productmodel',
            name='file_title',
        ),
    ]

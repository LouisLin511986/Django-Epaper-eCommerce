# Generated by Django 4.1.1 on 2022-10-16 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('indexapp', '0037_document'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='uploadedFile',
            field=models.FileField(upload_to='file/'),
        ),
    ]

# Generated by Django 4.0.5 on 2022-10-25 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('indexapp', '0044_alter_productmodel_pdescription'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodel',
            name='pimages',
            field=models.ImageField(blank=True, default=0, upload_to='image'),
        ),
        migrations.AlterField(
            model_name='productmodel',
            name='uploadedFile',
            field=models.FileField(blank=True, default='預設', null=True, upload_to='file'),
        ),
    ]

# Generated by Django 4.0.3 on 2022-05-15 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('indexapp', '0016_alter_productmodel_pimages'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodel',
            name='pimages',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
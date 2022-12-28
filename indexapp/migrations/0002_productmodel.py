# Generated by Django 4.0.3 on 2022-04-17 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('indexapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pname', models.CharField(default='', max_length=100)),
                ('pprice', models.IntegerField(default=0)),
                ('pimages', models.CharField(default='', max_length=100)),
                ('pdescription', models.TextField(blank=True, default='')),
            ],
        ),
    ]

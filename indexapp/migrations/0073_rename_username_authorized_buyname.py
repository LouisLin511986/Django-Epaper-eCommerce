# Generated by Django 4.1.1 on 2022-12-09 12:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('indexapp', '0072_alter_authorized_mod_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='authorized',
            old_name='username',
            new_name='buyname',
        ),
    ]

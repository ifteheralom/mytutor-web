# Generated by Django 2.0.7 on 2018-08-08 02:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_tutorprofile_edu_qualification'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tutorprofile',
            old_name='image',
            new_name='tutor_image',
        ),
    ]
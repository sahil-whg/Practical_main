# Generated by Django 3.1.2 on 2020-10-11 10:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('practical_main', '0010_userprofile_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='date',
        ),
    ]
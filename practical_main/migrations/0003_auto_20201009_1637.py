# Generated by Django 3.1.2 on 2020-10-09 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('practical_main', '0002_auto_20201009_1533'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='phone',
            field=models.IntegerField(default=0),
        ),
    ]

# Generated by Django 2.0.7 on 2018-07-22 12:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('languages', '0002_auto_20180722_1216'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Programmers',
            new_name='Programmer',
        ),
    ]

# Generated by Django 2.1 on 2018-08-29 13:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0009_auto_20180829_1347'),
    ]

    operations = [
        migrations.RenameField(
            model_name='report',
            old_name='user',
            new_name='author',
        ),
    ]
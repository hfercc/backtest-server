# Generated by Django 2.1 on 2018-09-04 04:06

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('report_id', models.AutoField(primary_key=True, serialize=False)),
                ('file', models.CharField(max_length=100)),
                ('status', models.IntegerField(default=0)),
                ('alpha_name', models.CharField(max_length=100)),
                ('add_time', models.DateTimeField(default=datetime.datetime.now)),
                ('error_message', models.CharField(blank=True, default='', max_length=100)),
                ('backtest_img', models.CharField(blank=True, default='', max_length=100)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-18 10:49
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Requests',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_time', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
    ]

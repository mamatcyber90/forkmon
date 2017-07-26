# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-26 21:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0015_mtfork'),
    ]

    operations = [
        migrations.CreateModel(
            name='UpdateLock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('in_use', models.BooleanField(default=False)),
                ('version', models.IntegerField(default=0)),
            ],
        ),
    ]

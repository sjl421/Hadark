# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-26 01:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0007_auto_20160725_1407'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='status',
            field=models.CharField(max_length=20, null=True),
        ),
    ]

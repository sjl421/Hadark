# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-22 03:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_auto_20160721_1428'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='codefile',
            name='job',
        ),
        migrations.AddField(
            model_name='job',
            name='files',
            field=models.ManyToManyField(to='mainapp.Document'),
        ),
        migrations.AddField(
            model_name='job',
            name='parameters',
            field=models.CharField(max_length=230, null=True),
        ),
        migrations.DeleteModel(
            name='CodeFile',
        ),
    ]
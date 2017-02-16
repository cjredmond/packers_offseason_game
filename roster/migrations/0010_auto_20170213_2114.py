# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-13 21:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roster', '0009_auto_20170213_2003'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='draft',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='account',
            name='final_cuts',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='account',
            name='free_agent',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='account',
            name='resign',
            field=models.BooleanField(default=False),
        ),
    ]
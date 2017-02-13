# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-10 20:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roster', '0005_draftplayer_college'),
    ]

    operations = [
        migrations.AlterField(
            model_name='draftplayer',
            name='cap_hit',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='freeagent',
            name='cap_hit',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='player',
            name='cap_hit',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='player',
            name='cut_savings',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-28 11:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='author',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='picture',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-02-26 03:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shopping', '0002_emailverfirecord'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='user_status',
            field=models.BooleanField(default=True, verbose_name='用户状态'),
        ),
    ]
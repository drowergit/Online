# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-04-10 02:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shopping', '0004_userprofile_pay'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='name_id',
            field=models.CharField(default='', max_length=20, verbose_name='身份证'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='real_name',
            field=models.CharField(default='', max_length=12, verbose_name='真实姓名'),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-12-19 09:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20191219_1537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='image',
            field=models.ImageField(default='D:\\intro-pbn\\python\\PersonalDashborad\\media\\panda.jpg', upload_to='media'),
        ),
    ]

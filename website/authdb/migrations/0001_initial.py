# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-05 05:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Student Name')),
                ('course', models.CharField(max_length=20, verbose_name='Course Name')),
                ('cgpa', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Students CGPA')),
                ('dob', models.DateField(verbose_name='Date of Birth')),
            ],
        ),
    ]

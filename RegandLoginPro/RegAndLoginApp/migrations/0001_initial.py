# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-09-27 17:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BranchInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_photo', models.ImageField(upload_to='static/images')),
                ('faculty_branch', models.CharField(max_length=50)),
                ('faculty_name', models.CharField(max_length=100)),
                ('faculty_description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='CommentData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback_id', models.IntegerField()),
                ('comment_name', models.CharField(max_length=100)),
                ('comment_text', models.CharField(max_length=500)),
                ('comment_date', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('t1', models.CharField(max_length=500)),
                ('image', models.ImageField(upload_to='images')),
                ('like', models.IntegerField()),
                ('date', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('username', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=100)),
                ('branch', models.CharField(max_length=100)),
                ('batch', models.IntegerField()),
                ('roll', models.CharField(max_length=10)),
            ],
        ),
    ]

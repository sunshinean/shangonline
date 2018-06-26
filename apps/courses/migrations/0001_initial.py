# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-06-13 15:09
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('orgs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='课程名称')),
                ('desc', models.CharField(max_length=200, verbose_name='课程简介')),
                ('detail', models.TextField(verbose_name='课程详情')),
                ('level', models.CharField(choices=[('cj', '初级'), ('zj', '中级'), ('gj', '高级')], default='cj', max_length=5, verbose_name='课程难度')),
                ('stunum', models.IntegerField(default=0, verbose_name='学习人数')),
                ('study_time', models.IntegerField(default=0, verbose_name='学习时长')),
                ('lesson_num', models.IntegerField(default=0, verbose_name='章节数')),
                ('category', models.CharField(choices=[('qd', '前端'), ('ht', '后台')], max_length=5, verbose_name='课程类别')),
                ('click_num', models.IntegerField(default=0, verbose_name='点击数')),
                ('love_num', models.IntegerField(default=0, verbose_name='收藏数')),
                ('image', models.ImageField(upload_to='course/%y/%m', verbose_name='课程图片')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('orginfo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orgs.OrgInfo', verbose_name='所属机构')),
                ('teacherinfo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orgs.TeacherInfo', verbose_name='所属讲师')),
            ],
            options={
                'verbose_name': '课程信息',
                'verbose_name_plural': '课程信息',
            },
        ),
        migrations.CreateModel(
            name='LessonInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='章节名称')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('courseinfo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.CourseInfo', verbose_name='所属课程')),
            ],
            options={
                'verbose_name': '章节信息',
                'verbose_name_plural': '章节信息',
            },
        ),
        migrations.CreateModel(
            name='SourceInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='资源名称')),
                ('file_addr', models.FileField(max_length=200, upload_to='source/%y/%m', verbose_name='资源地址')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('courseinfo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.CourseInfo', verbose_name='所属课程')),
            ],
            options={
                'verbose_name': '资源信息',
                'verbose_name_plural': '资源信息',
            },
        ),
        migrations.CreateModel(
            name='VideoInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='视频名称')),
                ('study_time', models.IntegerField(default=0, verbose_name='视频时长')),
                ('url', models.URLField(default='http://video.atguigu.com/ce182d3e92d24c08ada798ed75236efe/64240d5f98c849d7a48a701646314ef0-abb0a550e0a4e1bd89390a178f91a577-ld.mp4', verbose_name='视频连接')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('lessoninfo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.LessonInfo', verbose_name='所属章节')),
            ],
            options={
                'verbose_name': '视频信息',
                'verbose_name_plural': '视频信息',
            },
        ),
    ]

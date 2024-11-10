# Generated by Django 5.0.3 on 2024-11-06 05:04

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_userprofile_desc_userprofile_gexing'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='分类名称')),
                ('desc', models.TextField(blank=True, default='', max_length=200, verbose_name='分类描述')),
                ('add_date', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('pub_date', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
            ],
            options={
                'verbose_name': '博客分类',
                'verbose_name_plural': '博客分类',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='文章标签')),
                ('add_date', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('pub_date', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
            ],
            options={
                'verbose_name': '文章标签',
                'verbose_name_plural': '文章标签',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=61, verbose_name='文章标题')),
                ('desc', models.TextField(blank=True, default='', max_length=200, verbose_name='文章描述')),
                ('content', models.TextField(verbose_name='文章详情')),
                ('add_date', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('pub_date', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='作者')),
                ('tags', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.tag', verbose_name='文章标签')),
            ],
            options={
                'verbose_name': '文章',
                'verbose_name_plural': '文章',
            },
        ),
    ]

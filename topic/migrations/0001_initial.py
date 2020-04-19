# Generated by Django 2.1.4 on 2019-02-13 12:29

import django.core.validators
from django.db import migrations, models
import imagekit.models.fields
import mdeditor.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AgreeModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agreeTime', models.DateTimeField(auto_now_add=True, verbose_name='点赞时间')),
                ('status', models.PositiveIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(1)], verbose_name='是否已读')),
            ],
            options={
                'verbose_name_plural': '点赞模块',
                'verbose_name': '点赞模块',
            },
        ),
        migrations.CreateModel(
            name='Carousel_Model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='轮播标题')),
                ('slug', models.CharField(max_length=500, verbose_name='轮播内容')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='生成时间')),
                ('avatar', imagekit.models.fields.ProcessedImageField(blank=True, default='image/timg.jpg', height_field='avatarHeight', max_length=300, null=True, upload_to='carousel/%Y/%m', verbose_name='轮播图片', width_field='avatarWeight')),
                ('avatarWeight', models.PositiveIntegerField(default=800, verbose_name='个人头像宽度')),
                ('avatarHeight', models.PositiveIntegerField(default=250, verbose_name='个人头像高度')),
            ],
            options={
                'verbose_name_plural': '轮播内容',
                'ordering': ['-update_at'],
                'verbose_name': '轮播内容',
            },
        ),
        migrations.CreateModel(
            name='Create_Topic_Model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='标题')),
                ('draft_pk', models.CharField(blank=True, max_length=500, null=True, verbose_name='草稿id')),
                ('content', mdeditor.fields.MDTextField(verbose_name='文章内容(html版)')),
                ('pub_time', models.DateTimeField(auto_now_add=True, verbose_name='发布时间')),
                ('read_nums', models.IntegerField(default=0, verbose_name='阅读次数')),
                ('pictureUrl', models.CharField(blank=True, max_length=200, null=True, verbose_name='文章样图')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('top', models.IntegerField(blank=True, default='0', null=True, validators=[django.core.validators.MaxValueValidator(1), django.core.validators.MinValueValidator(0)], verbose_name='是否置顶(1表示置顶)')),
                ('slug', models.SlugField(blank=True, max_length=200, null=True, verbose_name='短标签')),
                ('agree', models.PositiveIntegerField(default=0, verbose_name='点赞次数')),
            ],
            options={
                'verbose_name_plural': '发表文章',
                'ordering': ('-pub_time',),
                'verbose_name': '发表文章',
            },
        ),
        migrations.CreateModel(
            name='Sort_Model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='文章分类/板块（内部）')),
                ('node', models.CharField(max_length=20, verbose_name='文章分类/板块（外部）')),
                ('description', models.TextField(verbose_name='板块描述')),
                ('sort_img', imagekit.models.fields.ProcessedImageField(blank=True, default='image/timg.jpg', height_field='sort_imgHeight', max_length=300, null=True, upload_to='sort/%Y/%m', verbose_name='分类图标', width_field='sort_imgWeight')),
                ('sort_imgWeight', models.PositiveIntegerField(default=150, verbose_name='个人头像宽度')),
                ('sort_imgHeight', models.PositiveIntegerField(default=150, verbose_name='个人头像高度')),
                ('post_number', models.IntegerField(default=0)),
                ('pub_time', models.DateTimeField(auto_now_add=True, verbose_name='分类序号(用时间区分)')),
                ('updated_time', models.DateTimeField(auto_now=True, verbose_name='更新板块时间')),
            ],
            options={
                'verbose_name_plural': '板块',
                'ordering': ['pub_time'],
                'verbose_name': '板块',
            },
        ),
    ]
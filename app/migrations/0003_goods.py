# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2019-03-15 06:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_classify'),
    ]

    operations = [
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lrp', models.CharField(max_length=20)),
                ('price', models.CharField(max_length=20)),
                ('img', models.CharField(max_length=100)),
                ('bigimg', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=255)),
                ('intro', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'mml_goods',
            },
        ),
    ]
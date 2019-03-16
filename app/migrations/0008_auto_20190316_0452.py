# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2019-03-16 04:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20190315_1240'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('isselect', models.BooleanField(default=True)),
                ('isdelete', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'mml_cart',
            },
        ),
        migrations.AddField(
            model_name='goods',
            name='name',
            field=models.CharField(default='弄啥嘞', max_length=20),
        ),
        migrations.AddField(
            model_name='cart',
            name='goods',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Goods'),
        ),
        migrations.AddField(
            model_name='cart',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.User'),
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-12 07:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ta_app', '0003_auto_20171112_1537'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='number_of_people',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='taskdetail',
            name='task_pk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='ta_app.Task'),
        ),
    ]

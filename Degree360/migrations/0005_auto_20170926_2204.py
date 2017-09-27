# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-26 20:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Degree360', '0004_auto_20170922_2138'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='question',
            unique_together=set([('section', 'text'), ('section', 'order')]),
        ),
        migrations.AlterUniqueTogether(
            name='questionsection',
            unique_together=set([('survey', 'description'), ('survey', 'order')]),
        ),
    ]
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cndapp', '0004_auto_20141107_1515'),
    ]

    operations = [
        migrations.AlterField(
            model_name='followupvisualacuityreading',
            name='value',
            field=models.CharField(max_length=4),
            preserve_default=True,
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cndapp', '0005_auto_20141107_1816'),
    ]

    operations = [
        migrations.AlterField(
            model_name='preopassessmentvisualacuityreading',
            name='value',
            field=models.CharField(max_length=4),
            preserve_default=True,
        ),
    ]

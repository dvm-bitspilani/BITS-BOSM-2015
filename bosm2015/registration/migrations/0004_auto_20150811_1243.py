# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0003_auto_20150811_1241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='coach',
            field=models.BooleanField(default=False),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0006_remove_check_used'),
    ]

    operations = [
        migrations.AddField(
            model_name='check',
            name='used',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]

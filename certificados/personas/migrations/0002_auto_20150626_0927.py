# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='telefono',
            field=models.CharField(max_length=20, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='persona',
            name='cedula',
            field=models.PositiveIntegerField(default=1, unique=True),
        ),
    ]

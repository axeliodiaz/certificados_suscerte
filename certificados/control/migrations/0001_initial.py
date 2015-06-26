# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Certificado',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('desde', models.DateField()),
                ('hasta', models.DateField()),
                ('revocacion', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'certificado',
            },
        ),
    ]

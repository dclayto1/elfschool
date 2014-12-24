# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('faculty_firstName', models.CharField(max_length=20)),
                ('faculty_lastName', models.CharField(max_length=20)),
                ('faculty_position', models.CharField(max_length=20)),
                ('faculty_email', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]

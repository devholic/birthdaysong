# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rankdata',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('chart', models.TextField()),
                ('year', models.PositiveSmallIntegerField()),
                ('week', models.PositiveSmallIntegerField()),
                ('title', models.TextField()),
                ('artist', models.TextField()),
                ('album', models.TextField()),
                ('youtube', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workload', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('run_date', models.DateTimeField(verbose_name=b'run date')),
                ('author', models.CharField(max_length=200)),
                ('content', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name=b'publish date')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]

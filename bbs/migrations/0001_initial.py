# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('key', models.TextField(blank=True)),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name=b'created')),
            ],
            options={
                'ordering': ['date'],
                'db_table': 'board',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name=b'posted')),
                ('text', models.TextField(blank=True)),
                ('board', models.ForeignKey(related_name='posts', to='bbs.Board')),
            ],
            options={
                'ordering': ['date'],
                'db_table': 'post',
            },
            bases=(models.Model,),
        ),
    ]

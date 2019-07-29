# -*- coding: utf-8 -*-


from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmailLog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('label', models.CharField(max_length=128)),
                ('subject', models.CharField(max_length=256)),
                ('sender', models.CharField(max_length=256)),
                ('recipients', models.TextField()),
                ('text', models.TextField(blank=True)),
                ('html', models.TextField(blank=True)),
                ('cc', models.TextField(blank=True)),
                ('bcc', models.TextField(blank=True)),
                ('created', models.DateTimeField(default=datetime.datetime.now)),
                ('headers', models.TextField(blank=True)),
            ],
        ),
    ]

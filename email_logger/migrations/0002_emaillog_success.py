# -*- coding: utf-8 -*-


from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('email_logger', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='emaillog',
            name='success',
            field=models.BooleanField(default=True),
        ),
    ]

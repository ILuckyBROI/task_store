# Generated by Django 3.2.12 on 2022-03-27 20:34

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_user_activation_key_expires'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='activation_key_expires',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 3, 28, 4, 34, 27, 309924, tzinfo=utc), null=True),
        ),
    ]

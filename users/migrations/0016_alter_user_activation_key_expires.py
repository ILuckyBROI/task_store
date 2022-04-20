# Generated by Django 3.2.12 on 2022-04-04 10:45

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0015_alter_user_activation_key_expires'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='activation_key_expires',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 4, 4, 18, 45, 52, 511321, tzinfo=utc), null=True),
        ),
    ]

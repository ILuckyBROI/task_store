# Generated by Django 3.2.12 on 2022-04-04 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_order_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='country',
            field=models.CharField(choices=[('1', 'Россия'), ('2', 'Казахстан'), ('3', 'Украина')], default='1', max_length=3, verbose_name='страна'),
        ),
    ]

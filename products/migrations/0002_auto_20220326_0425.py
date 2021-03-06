# Generated by Django 3.2.12 on 2022-03-26 01:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='availability',
            field=models.CharField(default='Есть в наличии', max_length=20),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(default='Новинки', on_delete=django.db.models.deletion.CASCADE, to='products.productcategory'),
        ),
    ]

# Generated by Django 3.0.7 on 2020-06-29 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_product_feature'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='summery',
            field=models.TextField(blank=True),
        ),
    ]

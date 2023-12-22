# Generated by Django 5.0 on 2023-12-20 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApplication', '0003_remove_order_products_order_products'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='products',
        ),
        migrations.AddField(
            model_name='order',
            name='products',
            field=models.ManyToManyField(to='MainApplication.product'),
        ),
    ]

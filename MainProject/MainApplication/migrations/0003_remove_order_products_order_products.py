# Generated by Django 5.0 on 2023-12-20 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApplication', '0002_member_order_user_customer_product_order_products_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='products',
        ),
        migrations.AddField(
            model_name='order',
            name='products',
            field=models.CharField(default=123, max_length=100),
            preserve_default=False,
        ),
    ]

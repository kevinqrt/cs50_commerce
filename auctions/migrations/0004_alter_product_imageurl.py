# Generated by Django 4.1.2 on 2022-10-31 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_product_remove_bid_products_remove_comments_products_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='imageURL',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
    ]

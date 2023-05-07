# Generated by Django 4.1.3 on 2022-11-05 12:27

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0007_product_watchlist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='watchlist',
            field=models.ManyToManyField(blank=True, related_name='productWatchlist', to=settings.AUTH_USER_MODEL),
        ),
    ]

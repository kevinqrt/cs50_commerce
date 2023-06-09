# Generated by Django 4.1.3 on 2022-11-11 21:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0011_remove_product_testinglist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bid',
            name='price',
        ),
        migrations.AddField(
            model_name='bid',
            name='bid',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='UserBid', to='auctions.bid'),
        ),
    ]

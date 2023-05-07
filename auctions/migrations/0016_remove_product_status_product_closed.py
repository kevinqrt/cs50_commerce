# Generated by Django 4.1.3 on 2022-11-19 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0015_product_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='status',
        ),
        migrations.AddField(
            model_name='product',
            name='closed',
            field=models.BooleanField(default=False),
        ),
    ]

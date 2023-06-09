# Generated by Django 4.1.2 on 2022-10-30 22:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_products_comments_bid'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('imageURL', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('description', models.CharField(max_length=64)),
                ('price', models.DecimalField(decimal_places=2, max_digits=9)),
                ('category', models.CharField(max_length=20)),
                ('expiration_date', models.DateTimeField()),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='bid',
            name='products',
        ),
        migrations.RemoveField(
            model_name='comments',
            name='products',
        ),
        migrations.DeleteModel(
            name='Products',
        ),
        migrations.AddField(
            model_name='bid',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='auctions.product'),
        ),
        migrations.AddField(
            model_name='comments',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='auctions.product'),
        ),
    ]

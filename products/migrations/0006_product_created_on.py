# Generated by Django 3.2 on 2022-06-29 06:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_product_onsale'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]

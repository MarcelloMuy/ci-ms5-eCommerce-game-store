# Generated by Django 3.2 on 2022-06-29 17:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_product_created_on'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='created_on',
        ),
    ]
# Generated by Django 5.0.4 on 2024-10-04 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_sellerproduct_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='categories',
            name='category_image',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to='categories/'),
        ),
    ]

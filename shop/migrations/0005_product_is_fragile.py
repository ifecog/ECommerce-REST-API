# Generated by Django 4.2.4 on 2023-09-15 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_fragile',
            field=models.BooleanField(default=False),
        ),
    ]
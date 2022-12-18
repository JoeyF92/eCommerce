# Generated by Django 4.1.4 on 2022-12-18 21:50

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0012_rename_owner_id_listing_owner_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='image',
            field=models.CharField(blank=True, max_length=100, validators=[django.core.validators.RegexValidator(regex='([^\\s]+(\\.(?i)(jpe?g|png|gif|bmp))$)')]),
        ),
    ]

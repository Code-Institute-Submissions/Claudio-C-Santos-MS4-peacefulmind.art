# Generated by Django 3.2 on 2021-06-22 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='communitycard',
            name='website',
            field=models.URLField(blank=True, db_index=True, max_length=254, unique=True),
        ),
    ]
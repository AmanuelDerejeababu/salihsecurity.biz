# Generated by Django 3.0.2 on 2021-04-08 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='title',
            field=models.CharField(default='', max_length=50),
        ),
    ]
# Generated by Django 3.0.2 on 2021-04-27 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0013_auto_20210427_1443'),
    ]

    operations = [
        migrations.AddField(
            model_name='land',
            name='content',
            field=models.TextField(default=''),
        ),
    ]
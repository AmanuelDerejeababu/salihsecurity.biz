# Generated by Django 3.0.2 on 2021-04-24 10:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0007_auto_20210420_1242'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='head',
        ),
    ]

# Generated by Django 3.0.2 on 2021-04-25 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0009_about'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='project',
            field=models.TextField(default=''),
        ),
    ]

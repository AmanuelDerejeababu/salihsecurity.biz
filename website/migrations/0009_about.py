# Generated by Django 3.0.2 on 2021-04-25 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0008_remove_post_head'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project', models.CharField(default='', max_length=50)),
                ('text', models.TextField(default='')),
            ],
        ),
    ]
# Generated by Django 3.0.2 on 2021-04-20 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_auto_20210420_1216'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('head', models.CharField(max_length=250)),
                ('image', models.ImageField(default='', upload_to='website/images')),
            ],
        ),
    ]
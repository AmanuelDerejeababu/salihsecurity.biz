# Generated by Django 3.0.2 on 2021-04-27 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0012_auto_20210427_1422'),
    ]

    operations = [
        migrations.CreateModel(
            name='Land',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(default='download_10.jpg', upload_to='website/images')),
            ],
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]

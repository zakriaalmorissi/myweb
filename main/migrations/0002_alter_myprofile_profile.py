# Generated by Django 5.0 on 2024-02-18 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myprofile',
            name='profile',
            field=models.ImageField(blank=True, upload_to='private/images/'),
        ),
    ]
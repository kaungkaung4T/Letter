# Generated by Django 3.2.9 on 2023-03-01 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0003_alter_profile_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appmodel',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='app_image'),
        ),
    ]
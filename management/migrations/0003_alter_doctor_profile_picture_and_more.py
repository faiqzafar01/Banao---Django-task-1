# Generated by Django 4.2.4 on 2023-08-17 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0002_alter_doctor_profile_picture_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]

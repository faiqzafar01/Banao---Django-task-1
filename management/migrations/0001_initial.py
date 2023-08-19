# Generated by Django 4.2.4 on 2023-08-17 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('profile_picture', models.ImageField(upload_to='images/')),
                ('user_name', models.CharField(max_length=20)),
                ('email_id', models.EmailField(blank=True, max_length=254, null=True)),
                ('password', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=20)),
                ('pincode', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('profile_picture', models.ImageField(upload_to='images/')),
                ('user_name', models.CharField(max_length=20)),
                ('email_id', models.EmailField(blank=True, max_length=254, null=True)),
                ('password', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=20)),
                ('pincode', models.IntegerField()),
            ],
        ),
    ]

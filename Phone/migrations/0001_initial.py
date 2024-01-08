# Generated by Django 5.0.1 on 2024-01-08 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
                ('storage', models.CharField(max_length=100)),
                ('ram', models.CharField(max_length=100)),
                ('frontCamera', models.CharField(max_length=100)),
                ('backCamera', models.CharField(max_length=100)),
                ('color', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('os', models.CharField(max_length=100)),
                ('isActive', models.BooleanField(default=True)),
            ],
        ),
    ]
# Generated by Django 5.0.2 on 2024-02-27 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='email',
            field=models.EmailField(blank=True, max_length=120, unique=True),
        ),
    ]
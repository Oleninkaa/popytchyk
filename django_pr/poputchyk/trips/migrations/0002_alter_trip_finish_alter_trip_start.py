# Generated by Django 5.0.6 on 2024-05-15 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='finish',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='trip',
            name='start',
            field=models.CharField(max_length=20),
        ),
    ]
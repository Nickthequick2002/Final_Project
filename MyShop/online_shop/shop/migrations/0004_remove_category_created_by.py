# Generated by Django 5.0.6 on 2024-07-21 18:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_category_created_by'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='created_by',
        ),
    ]

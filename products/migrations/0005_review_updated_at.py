# Generated by Django 3.2.25 on 2024-11-29 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]

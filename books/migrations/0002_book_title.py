# Generated by Django 5.1.4 on 2024-12-06 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='title',
            field=models.CharField(default='Test', max_length=100),
            preserve_default=False,
        ),
    ]

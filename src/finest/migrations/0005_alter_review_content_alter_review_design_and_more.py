# Generated by Django 5.1.3 on 2024-12-10 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finest', '0004_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='content',
            field=models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], default=1),
        ),
        migrations.AlterField(
            model_name='review',
            name='design',
            field=models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], default=1),
        ),
        migrations.AlterField(
            model_name='review',
            name='usability',
            field=models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], default=1),
        ),
    ]

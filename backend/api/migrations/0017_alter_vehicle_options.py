# Generated by Django 5.0.3 on 2024-09-21 21:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0016_parking_actions'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vehicle',
            options={'permissions': [('can_transfer_vehicle', 'Can transfer vehicle')]},
        ),
    ]

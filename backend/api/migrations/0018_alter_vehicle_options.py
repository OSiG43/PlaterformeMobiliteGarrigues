# Generated by Django 5.0.3 on 2024-09-22 21:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0017_alter_vehicle_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vehicle',
            options={'permissions': [('can_transfer_vehicle', 'Can transfer vehicle'), ('review_vehicle', 'Can access to the vehicle review')]},
        ),
    ]

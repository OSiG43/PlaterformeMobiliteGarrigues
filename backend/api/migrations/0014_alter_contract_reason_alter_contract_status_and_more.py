# Generated by Django 5.0.3 on 2024-04-09 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_alter_vehicle_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='reason',
            field=models.TextField(blank=True, choices=[('cdd', 'CDD'), ('cdi', 'CDI'), ('formation', 'Formation'), ('interim', 'Intérim'), ('aided_contract', 'Contrat aidé'), ('job_seeking', 'Recherche d’emploi'), ('part_time', 'Alternance')], null=True),
        ),
        migrations.AlterField(
            model_name='contract',
            name='status',
            field=models.CharField(choices=[('waiting', "En attente d'EDL"), ('pending', 'En cours'), ('over', 'Clôturé'), ('payed', 'Payé')], default='waiting', max_length=100),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='fleet_id',
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='status',
            field=models.CharField(choices=[('available', 'Disponible'), ('rented', 'A dispo'), ('maintenance', 'En maintenance')], default='available', max_length=20),
        ),
    ]

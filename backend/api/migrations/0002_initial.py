# Generated by Django 5.0.3 on 2024-05-06 22:47

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('api', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='contract',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='contracts_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='contract',
            name='referent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contracts_referent', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='contract',
            name='vehicle',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.vehicle'),
        ),
    ]
# Generated by Django 4.0.2 on 2022-02-06 20:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('import_data', '0002_remove_object_zmk_remove_registry_zmk'),
    ]

    operations = [
        migrations.AddField(
            model_name='registry',
            name='zmk',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rts', to='import_data.zmk'),
        ),
    ]

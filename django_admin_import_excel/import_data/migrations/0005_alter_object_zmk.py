# Generated by Django 4.0.2 on 2022-02-06 20:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('import_data', '0004_object_zmk'),
    ]

    operations = [
        migrations.AlterField(
            model_name='object',
            name='zmk',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='object', to='import_data.zmk'),
        ),
    ]

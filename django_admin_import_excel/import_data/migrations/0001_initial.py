# Generated by Django 4.0.2 on 2022-02-06 19:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ExcelFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='')),
                ('date_import', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Object',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=120)),
            ],
            options={
                'verbose_name_plural': 'Object',
            },
        ),
        migrations.CreateModel(
            name='Zmk',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
            ],
            options={
                'verbose_name_plural': 'Zmk',
            },
        ),
        migrations.CreateModel(
            name='Registry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.PositiveIntegerField(default=0)),
                ('weight', models.FloatField(default=0.0)),
                ('departure_date', models.DateField(blank=True, null=True)),
                ('receiving_date', models.DateField(blank=True, null=True)),
                ('object', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rts', to='import_data.object')),
                ('zmk', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rts', to='import_data.zmk')),
            ],
            options={
                'verbose_name_plural': 'RTS',
            },
        ),
        migrations.AddField(
            model_name='object',
            name='zmk',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='objects', to='import_data.zmk'),
        ),
    ]

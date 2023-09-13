# Generated by Django 3.0.7 on 2023-07-17 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cl_table', '0075_empsitelist'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppointmentStatus',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('value', models.CharField(blank=True, db_column='Status', max_length=150, null=True)),
                ('lable', models.CharField(blank=True, db_column='Display', max_length=150, null=True)),
                ('color', models.CharField(blank=True, db_column='Color', max_length=150, null=True)),
                ('border_color', models.CharField(blank=True, db_column='Border Color', max_length=150, null=True)),
                ('isactive', models.BooleanField(db_column='Isactive', default=True)),
                ('is_secstatus', models.BooleanField(db_column='Sec Status', default=False)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'db_table': 'AppointmentStatus',
            },
        ),
        migrations.CreateModel(
            name='TreatmentDuration',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('duration', models.TimeField()),
                ('isactive', models.BooleanField(db_column='Isactive', default=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'db_table': 'Treatment_Duration',
            },
        ),
    ]
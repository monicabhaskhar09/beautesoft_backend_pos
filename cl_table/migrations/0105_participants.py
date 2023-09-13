# Generated by Django 3.0.7 on 2023-07-17 14:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cl_table', '0104_dayendconfirmlog_termsandcondition'),
    ]

    operations = [
        migrations.CreateModel(
            name='Participants',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('isactive', models.BooleanField(default=True)),
                ('date_booked', models.DateField(blank=True, db_column='date_booked', null=True)),
                ('status', models.CharField(blank=True, choices=[('Booked', 'Booked'), ('Cancelled', 'Cancelled'), ('Arrived', 'Arrived'), ('Done', 'Done')], db_column='status', max_length=200, null=True)),
                ('remarks', models.CharField(blank=True, db_column='Remarks', max_length=255, null=True)),
                ('treatment_parentcode', models.CharField(blank=True, db_column='Treatment_ParentCode', max_length=20, null=True)),
                ('appt_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='cl_table.Appointment')),
                ('cust_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='cl_table.Customer')),
            ],
            options={
                'db_table': 'Participants',
            },
        ),
    ]

# Generated by Django 3.0.7 on 2023-07-17 15:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cl_table', '0112_invoicetemplate'),
        ('custom', '0067_manualinvoicesign'),
    ]

    operations = [
        migrations.CreateModel(
            name='EquipmentUsage',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('eq_number', models.CharField(blank=True, db_column='EQ_Number', default='', max_length=255, null=True)),
                ('title', models.CharField(blank=True, db_column='Project', default='', max_length=255, null=True)),
                ('company', models.CharField(blank=True, db_column='Company', default='', max_length=255, null=True)),
                ('contact_person', models.CharField(blank=True, db_column='ContactPerson', default='', max_length=255, null=True)),
                ('status', models.CharField(blank=True, db_column='Status', default='', max_length=255, null=True)),
                ('validity', models.CharField(blank=True, db_column='Validity', default='', max_length=255, null=True)),
                ('terms', models.CharField(blank=True, db_column='Terms', default='', max_length=255, null=True)),
                ('in_charge', models.CharField(blank=True, db_column='InCharge', default='', max_length=255, null=True)),
                ('remarks', models.CharField(blank=True, db_column='Remarks', default='', max_length=255, null=True)),
                ('footer', models.CharField(blank=True, db_column='Footer', default='', max_length=255, null=True)),
                ('active', models.CharField(blank=True, db_column='Active', default='active', max_length=255, null=True)),
                ('created_at', models.DateTimeField(db_column='Issue_Date', null=True)),
                ('is_issued', models.BooleanField(default=False)),
                ('cust_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='cl_table.Customer')),
                ('emp_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='cl_table.Employee')),
            ],
            options={
                'db_table': 'EquipmentUsage',
            },
        ),
    ]

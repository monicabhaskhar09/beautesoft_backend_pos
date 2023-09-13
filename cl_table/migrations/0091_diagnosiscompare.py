# Generated by Django 3.0.7 on 2023-07-17 14:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cl_table', '0090_diagnosis'),
    ]

    operations = [
        migrations.CreateModel(
            name='DiagnosisCompare',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('compare_code', models.CharField(blank=True, db_column='Compare_Code', max_length=100, null=True)),
                ('compare_remark', models.TextField(blank=True, db_column='Compare_Remark', null=True)),
                ('compare_datetime', models.DateTimeField(blank=True, db_column='Compare_DateTime', null=True)),
                ('compare_isactive', models.BooleanField(db_column='Compare_IsActive', default=True)),
                ('compare_user', models.CharField(blank=True, db_column='Compare_User', max_length=20, null=True)),
                ('cust_code', models.CharField(blank=True, db_column='Cust_Code', max_length=50, null=True)),
                ('diagnosis', models.ManyToManyField(to='cl_table.Diagnosis')),
                ('diagnosis1_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='diagnosis_compare_1', to='cl_table.Diagnosis')),
                ('diagnosis2_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='diagnosis_compare_2', to='cl_table.Diagnosis')),
            ],
            options={
                'db_table': 'Diagnosis_Compare',
            },
        ),
    ]

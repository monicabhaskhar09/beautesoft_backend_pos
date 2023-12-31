# Generated by Django 3.0.7 on 2023-07-17 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cl_table', '0111_outletrequestlog'),
    ]

    operations = [
        migrations.CreateModel(
            name='invoicetemplate',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, db_column='Name', max_length=200, null=True)),
                ('isactive', models.BooleanField(db_column='isActive', default=True)),
                ('checked', models.BooleanField(db_column='Checked', default=True)),
                ('type', models.CharField(blank=True, db_column='Type', max_length=200, null=True)),
            ],
            options={
                'db_table': 'invoicetemplate',
                'unique_together': {('name',)},
            },
        ),
    ]

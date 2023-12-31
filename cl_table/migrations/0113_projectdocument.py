# Generated by Django 3.0.7 on 2023-07-17 15:38

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('custom', '0071_posdiscquant'),
        ('cl_table', '0112_invoicetemplate'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectDocument',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('filename', models.CharField(blank=True, db_column='filename', max_length=500, null=True)),
                ('document_name', models.CharField(blank=True, db_column='document_name', max_length=500, null=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('file', models.FileField(upload_to='img')),
                ('photo', models.BooleanField(blank=True, db_column='photo', null=True)),
                ('selected', models.BooleanField(blank=True, db_column='selected', null=True)),
                ('customer_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='cl_table.Customer')),
                ('fk_project', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='custom.ProjectModel')),
            ],
            options={
                'db_table': 'ProjectDocument',
            },
        ),
    ]

# Generated by Django 3.0.7 on 2023-09-04 19:23

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cl_table', '0117_auto_20230904_1922'),
    ]

    operations = [
        migrations.CreateModel(
            name='StaffDocument',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('filename', models.CharField(blank=True, db_column='filename', max_length=500, null=True)),
                ('document_name', models.CharField(blank=True, db_column='document_name', max_length=500, null=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('file', models.FileField(upload_to='img')),
                ('employee', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='cl_table.Employee')),
            ],
            options={
                'db_table': 'StaffDocument',
            },
        ),
    ]
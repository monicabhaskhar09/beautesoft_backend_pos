# Generated by Django 3.0.7 on 2023-07-17 14:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('custom', '0018_projectmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActivityModel',
            fields=[
                ('id', models.AutoField(db_column='Activity_ID', primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, db_column='Activity_Title', default='', max_length=255, null=True)),
                ('name', models.CharField(blank=True, db_column='Creator_Name', default='', max_length=255, null=True)),
                ('activity_type', models.CharField(blank=True, db_column='Activity_Type', default='', max_length=255, null=True)),
                ('active', models.CharField(blank=True, db_column='Active', default='active', max_length=255, null=True)),
                ('created_at', models.DateTimeField(db_column='Activity_Date', null=True)),
                ('fk_project', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='custom.ProjectModel')),
            ],
            options={
                'db_table': 'Project_Activities',
            },
        ),
    ]

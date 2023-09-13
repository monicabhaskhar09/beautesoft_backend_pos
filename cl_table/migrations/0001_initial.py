# Generated by Django 3.0.7 on 2023-07-14 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('itm_id', models.AutoField(primary_key=True, serialize=False)),
                ('itm_desc', models.CharField(blank=True, max_length=40, null=True)),
                ('itm_code', models.CharField(blank=True, max_length=10, null=True)),
                ('itm_isactive', models.BooleanField(default=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'db_table': 'City',
            },
        ),
        migrations.CreateModel(
            name='CommType',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('comm_type_code', models.CharField(blank=True, db_column='Comm_Type_Code', max_length=20, null=True)),
                ('comm_type_desc', models.CharField(blank=True, db_column='Comm_Type_Desc', max_length=50, null=True)),
                ('comm_type_active', models.BooleanField(db_column='Comm_Type_Active', default=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'db_table': 'Comm_Type',
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('itm_id', models.AutoField(primary_key=True, serialize=False)),
                ('itm_desc', models.CharField(blank=True, max_length=40, null=True)),
                ('itm_code', models.CharField(blank=True, max_length=10, null=True)),
                ('itm_isactive', models.BooleanField(default=True)),
                ('phonecode', models.CharField(blank=True, db_column='phoneCode', max_length=20, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'db_table': 'Country',
            },
        ),
        migrations.CreateModel(
            name='CustomerClass',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('class_code', models.CharField(blank=True, db_column='Class_Code', max_length=50, null=True)),
                ('class_desc', models.CharField(blank=True, db_column='Class_Desc', max_length=50, null=True)),
                ('class_isactive', models.BooleanField(blank=True, db_column='Class_Isactive', default=True, null=True)),
                ('class_product', models.FloatField(db_column='Class_Product')),
                ('class_service', models.FloatField(db_column='Class_Service')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('autoclassamount', models.IntegerField(blank=True, db_column='autoclassamount', null=True)),
                ('package_code', models.CharField(blank=True, db_column='Package_Code', max_length=50, null=True)),
            ],
            options={
                'db_table': 'Customer_Class',
            },
        ),
        migrations.CreateModel(
            name='CustomerTitle',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('itm_code', models.CharField(blank=True, db_column='ITM_CODE', max_length=20, null=True)),
                ('itm_desc', models.CharField(blank=True, db_column='ITM_DESC', max_length=20, null=True)),
                ('seq', models.FloatField(db_column='SEQ')),
                ('isactive', models.BooleanField(db_column='ISACTIVE')),
            ],
            options={
                'db_table': 'Customer_Title',
            },
        ),
        migrations.CreateModel(
            name='Days',
            fields=[
                ('itm_id', models.AutoField(db_column='ITM_ID', primary_key=True, serialize=False)),
                ('itm_code', models.CharField(blank=True, db_column='ITM_CODE', max_length=50, null=True)),
                ('itm_name', models.CharField(blank=True, db_column='ITM_NAME', max_length=50, null=True)),
                ('itm_isactive', models.BooleanField(db_column='ITM_ISACTIVE', default=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'db_table': 'DAYS',
            },
        ),
        migrations.CreateModel(
            name='EmpEpf',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('emp_code', models.CharField(blank=True, db_column='EMP_CODE', max_length=20, null=True)),
                ('emp_epf_employee', models.FloatField(db_column='EMP_EPF_EMPLOYEE')),
                ('emp_epf_employer', models.FloatField(db_column='EMP_EPF_EMPLOYER')),
            ],
            options={
                'db_table': 'EMP_EPF',
            },
        ),
        migrations.CreateModel(
            name='EmpSocso',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('emp_code', models.CharField(blank=True, db_column='Emp_Code', max_length=50, null=True)),
                ('emp_socso_employee', models.FloatField(blank=True, db_column='Emp_SOCSO_Employee', null=True)),
                ('emp_socso_employer', models.FloatField(blank=True, db_column='Emp_SOCSO_Employer', null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'db_table': 'Emp_SOCSO',
            },
        ),
        migrations.CreateModel(
            name='EmpType',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('type_code', models.CharField(blank=True, db_column='TYPE_CODE', max_length=20, null=True)),
                ('type_desc', models.CharField(blank=True, db_column='TYPE_DESC', max_length=50, null=True)),
                ('type_isactive', models.BooleanField(blank=True, db_column='TYPE_ISACTIVE', default=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'db_table': 'EMP_TYPE',
            },
        ),
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('itm_id', models.AutoField(primary_key=True, serialize=False)),
                ('itm_name', models.CharField(blank=True, max_length=20, null=True)),
                ('itm_isactive', models.BooleanField(default=True)),
                ('itm_code', models.CharField(blank=True, db_column='ITM_CODE', max_length=50, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'db_table': 'Gender',
            },
        ),
        migrations.CreateModel(
            name='ItemStatus',
            fields=[
                ('itm_id', models.AutoField(primary_key=True, serialize=False)),
                ('status_code', models.CharField(blank=True, db_column='Status_Code', max_length=50, null=True)),
                ('status_desc', models.CharField(blank=True, db_column='Status_Desc', max_length=255, null=True)),
                ('status_short_desc', models.CharField(blank=True, db_column='Status_Short_Desc', max_length=255, null=True)),
                ('itm_isactive', models.BooleanField(db_column='itm_IsActive', default=True)),
                ('status_group_code', models.CharField(blank=True, db_column='Status_Group_Code', max_length=20, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'db_table': 'item_status',
            },
        ),
        migrations.CreateModel(
            name='Maritalstatus',
            fields=[
                ('itm_id', models.AutoField(primary_key=True, serialize=False)),
                ('itm_name', models.CharField(blank=True, max_length=20, null=True)),
                ('itm_isactive', models.BooleanField(default=True)),
                ('itm_code', models.IntegerField(blank=True, db_column='ITM_CODE', null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'db_table': 'MaritalStatus',
            },
        ),
        migrations.CreateModel(
            name='Nationality',
            fields=[
                ('itm_id', models.AutoField(primary_key=True, serialize=False)),
                ('itm_name', models.CharField(blank=True, max_length=50, null=True)),
                ('itm_isactive', models.BooleanField(default=True)),
                ('itm_code', models.CharField(blank=True, db_column='ITM_CODE', max_length=50, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'db_table': 'NATIONALITY',
            },
        ),
        migrations.CreateModel(
            name='Races',
            fields=[
                ('itm_id', models.AutoField(primary_key=True, serialize=False)),
                ('itm_name', models.CharField(blank=True, max_length=20, null=True)),
                ('itm_isactive', models.BooleanField(default=True)),
                ('itm_code', models.CharField(blank=True, db_column='ITM_CODE', max_length=50, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'db_table': 'Races',
            },
        ),
        migrations.CreateModel(
            name='Religious',
            fields=[
                ('itm_id', models.AutoField(primary_key=True, serialize=False)),
                ('itm_name', models.CharField(blank=True, max_length=20, null=True)),
                ('itm_isactive', models.BooleanField(default=True)),
                ('itm_code', models.CharField(blank=True, db_column='ITM_CODE', max_length=50, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'db_table': 'Religious',
            },
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('itm_id', models.AutoField(db_column='itm_ID', primary_key=True, serialize=False)),
                ('itm_desc', models.CharField(blank=True, max_length=40, null=True)),
                ('itm_code', models.CharField(blank=True, max_length=10, null=True)),
                ('itm_isactive', models.BooleanField(default=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'db_table': 'State',
            },
        ),
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('source_code', models.CharField(db_column='Source_Code', max_length=20, null=True)),
                ('source_desc', models.CharField(blank=True, db_column='Source_Desc', max_length=100, null=True)),
                ('source_isactive', models.BooleanField(db_column='Source_IsActive', default=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'db_table': 'Source',
                'unique_together': {('source_code',)},
            },
        ),
    ]
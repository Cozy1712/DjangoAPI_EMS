# Generated by Django 5.1.7 on 2025-03-09 12:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('EmployeeApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='departments',
            old_name='DepartmentsId',
            new_name='DepartmentId',
        ),
        migrations.RenameField(
            model_name='departments',
            old_name='departmentName',
            new_name='DepartmentName',
        ),
    ]

# Generated by Django 5.0 on 2024-03-04 15:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app_securevault', '0004_remove_educationaldetails_foreignkey_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sign_in',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Sign_up',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('mobile', models.IntegerField()),
                ('email', models.EmailField(max_length=100)),
                ('address', models.CharField(max_length=255)),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='HealthRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=100)),
                ('dob', models.DateField()),
                ('age', models.IntegerField()),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], max_length=10)),
                ('conditions', models.TextField(blank=True)),
                ('allergies', models.TextField(blank=True)),
                ('medications', models.TextField(blank=True)),
                ('surgeries', models.TextField(blank=True)),
                ('family_history', models.TextField(blank=True)),
                ('symptoms', models.TextField(blank=True)),
                ('symptoms_duration', models.CharField(blank=True, max_length=100)),
                ('symptoms_severity', models.CharField(blank=True, max_length=100)),
                ('diet', models.TextField(blank=True)),
                ('exercise', models.TextField(blank=True)),
                ('insurance_provider', models.CharField(blank=True, max_length=100)),
                ('policy_number', models.CharField(blank=True, max_length=100)),
                ('emergency_name', models.CharField(blank=True, max_length=100)),
                ('emergency_relationship', models.CharField(blank=True, max_length=100)),
                ('emergency_phone', models.CharField(blank=True, max_length=20)),
                ('additional_comments', models.TextField(blank=True)),
                ('foreignkey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_securevault.sign_in')),
            ],
        ),
        migrations.CreateModel(
            name='FinancialDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('income', models.DecimalField(decimal_places=2, max_digits=15)),
                ('savings', models.DecimalField(decimal_places=2, max_digits=15)),
                ('assets', models.DecimalField(decimal_places=2, max_digits=15)),
                ('debts', models.DecimalField(decimal_places=2, max_digits=15)),
                ('expenses', models.DecimalField(decimal_places=2, max_digits=15)),
                ('credit_score', models.CharField(blank=True, max_length=20)),
                ('aadhar_no', models.CharField(blank=True, max_length=12)),
                ('pan_no', models.CharField(blank=True, max_length=10)),
                ('bank_account_no', models.CharField(max_length=20)),
                ('credit_card_no', models.CharField(max_length=20)),
                ('additional_info', models.TextField(blank=True)),
                ('foreignkey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_securevault.sign_in')),
            ],
        ),
        migrations.CreateModel(
            name='EducationalDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('degree', models.CharField(max_length=100)),
                ('university', models.CharField(max_length=100)),
                ('major', models.CharField(max_length=100)),
                ('graduation_year', models.CharField(max_length=4)),
                ('gpa', models.CharField(blank=True, max_length=10)),
                ('twelth_marks_percentage', models.CharField(blank=True, max_length=10)),
                ('tenth_marks_percentage', models.CharField(blank=True, max_length=10)),
                ('certifications', models.TextField(blank=True)),
                ('additional_info', models.TextField(blank=True)),
                ('foreignkey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_securevault.sign_in')),
            ],
        ),
    ]

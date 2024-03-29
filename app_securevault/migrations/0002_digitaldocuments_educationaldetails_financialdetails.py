# Generated by Django 5.0 on 2024-02-21 14:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_securevault', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DigitalDocuments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aadhar', models.FileField(blank=True, upload_to='')),
                ('pan_card', models.FileField(blank=True, upload_to='')),
                ('driving_license', models.FileField(blank=True, upload_to='')),
                ('health_insurance', models.FileField(blank=True, upload_to='')),
                ('educational_certificate_1', models.FileField(blank=True, upload_to='')),
                ('educational_certificate_2', models.FileField(blank=True, upload_to='')),
                ('educational_certificate_3', models.FileField(blank=True, upload_to='')),
                ('other_document_1', models.FileField(blank=True, upload_to='')),
                ('other_document_2', models.FileField(blank=True, upload_to='')),
                ('other_document_3', models.FileField(blank=True, upload_to='')),
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
    ]

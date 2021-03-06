# Generated by Django 3.2.6 on 2021-08-31 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=12, null=True)),
                ('last_name', models.CharField(blank=True, max_length=12, null=True)),
                ('gender', models.CharField(blank=True, choices=[('1', 'Female'), ('2', 'Male'), ('3', 'Binary')], max_length=8, null=True)),
                ('age', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=10, null=True)),
                ('nationality', models.CharField(blank=True, choices=[('1', 'Rwandan'), ('2', 'Kenyan'), ('3', 'Ugandan'), ('4', 'SouthSudanese'), ('5', 'Sudanes')], max_length=15, null=True)),
                ('natioinal_id', models.CharField(blank=True, max_length=20, null=True)),
                ('email_address', models.CharField(blank=True, max_length=20, null=True)),
                ('academic_level', models.CharField(blank=True, choices=[('1', 'Bachelors'), ('2', 'Diploma'), ('3', 'Certificate'), ('4', 'High School Diploma')], max_length=20, null=True)),
                ('admission_date', models.DateField(blank=True, null=True)),
                ('academic_documents', models.FileField(blank=True, null=True, upload_to='files/')),
                ('medical_form', models.FileField(blank=True, null=True, upload_to='files/')),
                ('profile_pic', models.ImageField(null=True, upload_to='images/')),
                ('district', models.CharField(blank=True, max_length=12, null=True)),
                ('laptop_serial_number', models.CharField(blank=True, max_length=6, null=True)),
            ],
        ),
    ]

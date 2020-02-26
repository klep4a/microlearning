# Generated by Django 3.0.3 on 2020-02-24 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('microlearning', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='type',
            field=models.CharField(choices=[('Allergy & Immunology', 'Allergy & Clinical Immunology'), ('Anesthesiology', 'Anesthesiology'), ('Business of Medicine', 'Business of Medicine'), ('Cardiology', 'Cardiology'), ('Critical Care', 'Critical Care'), ('Dermatology', 'Dermatology'), ('Diabetes & Endocrinology', 'Diabetes & Endocrinology'), ('Emergency Medicine', 'Emergency Medicine'), ('Family Medicine', 'Family Medicine'), ('Gastroenterology', 'Gastroenterology'), ('General Surgery', 'General Surgery'), ('Hematology-Oncology', 'Oncology'), ('HIV/AIDS', 'HIV/AIDS'), ('Hospital Medicine', 'Hospital Medicine'), ('Infectious Diseases', 'Infectious Diseases'), ('Internal Medicine', 'Internal Medicine'), ('Nephrology', 'Nephrology'), ('Neurology', 'Neurology'), ("Ob/Gyn & Women's Health", "Ob/Gyn & Women's Health"), ('Oncology', 'Oncology'), ('Ophthalmology', 'Ophthalmology'), ('Orthopedics', 'Orthopedics'), ('Pathology & Lab Medicine', 'Pathology & Lab Medicine'), ('Pediatrics', 'Pediatrics'), ('Plastic Surgery', 'Plastic Surgery'), ('Psychiatry', 'Psychiatry'), ('Public Health', 'Public Health & Prevention'), ('Pulmonary Medicine', 'Pulmonary Medicine'), ('Radiology', 'Radiology'), ('Rheumatology', 'Rheumatology'), ('Transplantation', 'Transplantation'), ('Urology', 'Urology')], default='theory', max_length=50),
        ),
    ]

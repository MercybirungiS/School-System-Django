from django.db import models

from django.db.models.fields import files

# Create your models here.
class StudentDetails(models.Model):
    first_name=models.CharField(max_length=12, blank=True, null=True)
    last_name=models.CharField(max_length=12, blank=True, null=True)
    gender_choice=(
        ('1','Female'),
        ('2','Male'),
        ('3','Binary')
    )
    gender=models.CharField(max_length=8,choices=gender_choice, blank=True, null=True)
    age=models.PositiveSmallIntegerField( blank=True, null=True)
    phone_number=models.CharField(max_length=10, blank=True, null=True)
    nationality_choice=(
        ('1','Rwandan'),
        ('2','Kenyan'),
        ('3','Ugandan'),
        ('4','SouthSudanese'),
        ('5','Sudanes')
    )
    nationality=models.CharField(max_length=15,choices=nationality_choice, blank=True, null=True)
    natioinal_id=models.CharField(max_length=20, blank=True, null=True)
    email_address=models.CharField( max_length=20,blank=True, null=True)
    academic_qualification_choice=(
        ('1' ,'Bachelors'),
        ('2','Diploma'),
        ('3' ,'Certificate'),
        ('4','High School Diploma')
    )
    academic_level=models.CharField(max_length=20,choices=academic_qualification_choice, blank=True, null=True)
    admission_date=models.DateField( blank=True, null=True)
    academic_documents=models.FileField(upload_to="files/", blank=True, null=True)
    medical_form=models.FileField(upload_to="files/", blank=True, null=True)
    profile_pic=models.ImageField(upload_to="images/", null=True)
    district=models.CharField(max_length=12, blank=True, null=True)
    laptop_serial_number=models.CharField(max_length=6,null=True,blank=True)


   
  
   
    
 
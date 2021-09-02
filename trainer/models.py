from django.db import models
from django.db.models.fields import files

# Create your models here.
class Trainer(models.Model):
    first_name=models.CharField(max_length=12, blank=True, null=True)
    last_name=models.CharField(max_length=12, blank=True, null=True)
    gender_choice=(
        ('1','Female'),
        ('2','Male'),
        ('3','Binary')
    )
    gender=models.CharField(max_length=8,choices=gender_choice,blank=True, null=True)
    phone_number=models.CharField(max_length=10, blank=True, null=True)
    email_address=models.CharField( max_length=20,blank=True, null=True)
    contract=models.FileField(upload_to="files/", blank=True, null=True)
    resume=models.FileField(upload_to="files/", blank=True, null=True)
    salary=models.PositiveBigIntegerField( blank=True, null=True)
    profile_pic=models.ImageField(upload_to="images/",blank=True, null=True)
    syllabus=models.CharField(max_length=15, blank=True, null=True)
    company=models.CharField(max_length=12, blank=True, null=True)
    natioinal_id=models.CharField(max_length=20, blank=True, null=True)
    


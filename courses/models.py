from django.db import models
from django.db.models.fields import files


# Create your models here.

class Courses(models.Model):
    course_name=models.CharField(max_length=20, blank=True, null=True)
    course_code=models.CharField(max_length=12, blank=True, null=True)
    trainer=models.CharField(max_length=20, blank=True, null=True)
    course_description=models.TextField(blank=True, null=True)
    stack=models.CharField(max_length=20, blank=True, null=True)
    course_material=models.FileField(upload_to="files/", blank=True, null=True)
    course_duration=models.CharField(max_length=12, blank=True, null=True)
    
    

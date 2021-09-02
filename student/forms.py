from django import forms
from django.db import models
from django.forms import fields
from .models import StudentDetails

class StudentsForm(forms.ModelForm):
    class Meta:
        model=StudentDetails
        fields="__all__"
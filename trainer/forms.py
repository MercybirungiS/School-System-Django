from django import forms
from django.db import models
from django.forms import fields
from .models import Trainer

class TrainerForm(forms.ModelForm):
    class Meta:
        model=Trainer
        fields="__all__"
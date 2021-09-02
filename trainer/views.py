from django import forms

from django.shortcuts import render
from .forms import TrainerForm
from .models import Trainer
from trainer.models import Trainer

# Create your views here.
def register_trainer (request):
    if request.method=="POST":
       form=TrainerForm(request.POST , request.FILES)
       if form.is_valid():
            form.save()
       else:
            print(form.errors)
    else:
        form=TrainerForm()
    return render(request,"register_trainer.html",{"form":form})

def trainers_list(request):
    trainers=Trainer.objects.all()
    return render(request,"trainer_list.html",{"trainers" :trainers})



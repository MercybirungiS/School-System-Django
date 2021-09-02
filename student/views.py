from student.models import StudentDetails
from django import forms

from django.shortcuts import render
from .forms import StudentsForm
from .models import StudentDetails

# Create your views here.
def register_student (request):
    if request.method=="POST":
       form=StudentsForm(request.POST , request.FILES)
       if form.is_valid():
            form.save()
       else:
            print(form.errors)
    else:
        form=StudentsForm()
    return render(request,"registerstudent.html",{"form":form})

def student_list(request):
    students=StudentDetails.objects.all()
    return render(request,"student_list.html",{"students" :students})


from student.models import StudentDetails
from django import forms

from django.shortcuts import redirect, render
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

def edit_profile(request, id):
    student= StudentDetails.objects.get(id=id)
    if request.method == "POST":
        form=StudentsForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect("student-profile", id=student.id)
    else:
        form= StudentsForm(instance=student)
        return render(request,"edit_profile.html", {"form":form})

def student_profile(request,id):
    student=StudentDetails.objects.get(id=id)
    return render (request,"student_profile.html",{"student":student})

def delete_student(request,id):
    student=StudentDetails.objects.get(id=id)
    student.delete()
    return redirect("student_list")




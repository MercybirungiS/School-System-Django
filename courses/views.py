from django import forms
from django.shortcuts import render
from .forms import CoursesForm
from .models import Courses
from courses.models import Courses



# Create your views here.
def register_course (request):
    if request.method=="POST":
       form=CoursesForm(request.POST , request.FILES)
       if form.is_valid():
            form.save()
       else:
            print(form.errors)
    else:
        form=CoursesForm()
    return render(request,"register_course.html",{"form":form})

def courses_list(request):
    courses=Courses.objects.all()
    return render(request,"course_list.html",{"courses" :courses})



    



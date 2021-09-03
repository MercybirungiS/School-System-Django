from django.shortcuts import render
from student.models import StudentDetails
from trainer.models import Trainer
from courses.models import Courses

# Create your views here.
def home(request):
    student=StudentDetails.objects.count()
    trainer=Trainer.objects.count()
    course=Courses.objects.count()
    data={'students':student,'trainer':trainer,'courses':course}
    return render(request,"home_page.html",data)


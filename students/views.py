from django.shortcuts import render, HttpResponse
from .models import Student

# Create your views here.
def student(request):
    students = Student.objects.all()
    res = ''
    for stud in students:
        res += f'{stud.surname} {stud.name} {stud.second_name}'

    return HttpResponse(res)
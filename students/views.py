from django . shortcuts import render , redirect
from.models import Student
from django.db.models import Q
from django.contrib.auth.decorators import login_required
@login_required
def home(request):
    query = request.GET.get('search',)
    if query:
        students = Student.objects.filter(
            name__icontains=query) 
    else:
        students=Student.objects.all()
    return render(request,'home.html',{'students': students ,'query':query})
def add_student(request):
    if request.method == "POST":
        name = request.POST['name']
        age = request.POST['age']
        city  = request.POST['city']
        Student.objects.create(
            name=name,  
            age=age,
            city=city
        )
        return redirect('home')
    return render(request, 
     'add_student.html')

def edit_student(request, student_id):
    student = Student.objects.get(id=student_id)
    if request.method == "POST":
        student.name = request.POST['name']
        student.age = request.POST['age']
        student.city = request.POST['city']
        student.save()
        return redirect('home')
    return render(request, 'edit_student.html', {'student': student})
def delete_student(request, student_id):
        student = Student.objects.get(id=student_id)
        student.delete()
        return redirect('home')

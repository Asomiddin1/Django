from django.shortcuts import render, get_object_or_404, redirect
from .models import Student

def student_list(request):
    students = Student.objects.all()
    context = {
        'students': students
    }
    return render(request, 'students/student_list.html', context)

def student_detail(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    context = {
        'student': student
    }
    return render(request, 'students/student_detail.html', context)

def student_redirect(request):
    # Talabalar ro'yxatiga (student_list) yo'naltiruvchi redirect funksiya
    return redirect('student_list')


    
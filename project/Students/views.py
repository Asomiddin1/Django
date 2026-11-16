from django.shortcuts import render, get_object_or_404, redirect
from .models import Student
from .forms import StudentForm

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

def student_add(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    context = {'form': form}
    return render(request, 'students/student_add.html', context)

def student_edit(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_detail', student_id=student.id)
    else:
        form = StudentForm(instance=student)
    context = {
        'form': form,
        'student': student
    }
    return render(request, 'students/student_edit.html', context)

# Eskiroq murojaatlar uchun alias
student_create = student_add

def student_redirect(request):
    return redirect('student_list')

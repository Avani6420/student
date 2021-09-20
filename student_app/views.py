from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import student
from .form import Student_Form


def display(request):
    show = student.objects.all()
    return render(request, 'index.html', {'show': show})


def stud_create(request):
    if request.method == 'POST':
        form = Student_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/show')
    else:
        form = Student_Form()
    return render(request, 'add_stud.html', {'form': form})


def stud_display(request):
    return render(request, 'index.html')


def edit(request, id):
    stud = student.objects.get(id=id)
    return render(request, 'update.html', {'stud': stud})


def update(request, id):
    data = student.objects.get(id=id)
    if request.method == 'POST':
        stud = Student_Form(request.POST, request.FILES, instance=data)
        if stud.is_valid():
            stud.save()
            return redirect('/show')
    else:
        stud = Student_Form()
    return render(request, 'update.html', {'stud': stud})


def destroy(request, id):
    stud = student.objects.get(id=id)
    stud.delete()
    return redirect('/show')

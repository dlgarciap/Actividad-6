from django.shortcuts import render, get_object_or_404, redirect
from .models import Student, Publisher, Authorizer, Publication
from .forms import (
    StudentForm, PublisherForm, AuthorizerForm,
    PublicationForm, UserRegisterForm
)
from django.contrib.auth.models import User

# -----------------------------------------
#  CRUD ESTUDIANTES
# -----------------------------------------
def students_list(request):
    students = Student.objects.all()
    return render(request, 'revista/students_list.html', {'students': students})

def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('students_list')
    else:
        form = StudentForm()
    return render(request, 'revista/student_form.html', {'form': form})

def student_edit(request, pk):
    estudiante = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=estudiante)
        if form.is_valid():
            form.save()
            return redirect('students_list')
    else:
        form = StudentForm(instance=estudiante)
    return render(request, 'revista/student_form.html', {'form': form})

def student_detail(request, pk):
    estudiante = get_object_or_404(Student, pk=pk)
    return render(request, 'revista/student_detail.html', {'estudiante': estudiante})


# -----------------------------------------
#  CRUD PUBLICADORES
# -----------------------------------------
def publishers_list(request):
    publishers = Publisher.objects.all()
    return render(request, 'revista/publishers_list.html', {'publishers': publishers})

def publisher_create(request):
    if request.method == 'POST':
        form = PublisherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('publishers_list')
    else:
        form = PublisherForm()
    return render(request, 'revista/publisher_form.html', {'form': form})

def publisher_edit(request, pk):
    publisher = get_object_or_404(Publisher, pk=pk)
    if request.method == 'POST':
        form = PublisherForm(request.POST, instance=publisher)
        if form.is_valid():
            form.save()
            return redirect('publishers_list')
    else:
        form = PublisherForm(instance=publisher)
    return render(request, 'revista/publisher_form.html', {'form': form})

def publisher_detail(request, pk):
    publisher = get_object_or_404(Publisher, pk=pk)
    return render(request, 'revista/publisher_detail.html', {'publisher': publisher})


# -----------------------------------------
#  CRUD AUTORIZADORES
# -----------------------------------------
def authorizers_list(request):
    authorizers = Authorizer.objects.all()
    return render(request, 'revista/authorizers_list.html', {'authorizers': authorizers})

def authorizer_create(request):
    if request.method == 'POST':
        form = AuthorizerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('authorizers_list')
    else:
        form = AuthorizerForm()
    return render(request, 'revista/authorizer_form.html', {'form': form})

def authorizer_edit(request, pk):
    authorizer = get_object_or_404(Authorizer, pk=pk)
    if request.method == 'POST':
        form = AuthorizerForm(request.POST, instance=authorizer)
        if form.is_valid():
            form.save()
            return redirect('authorizers_list')
    else:
        form = AuthorizerForm(instance=authorizer)
    return render(request, 'revista/authorizer_form.html', {'form': form})

def authorizer_detail(request, pk):
    authorizer = get_object_or_404(Authorizer, pk=pk)
    return render(request, 'revista/authorizer_detail.html', {'authorizer': authorizer})


# -----------------------------------------
#  CRUD PUBLICACIONES
# -----------------------------------------
def publications_list(request):
    publications = Publication.objects.all()
    return render(request, 'revista/publications_list.html', {'publications': publications})

def publication_create(request):
    if request.method == 'POST':
        form = PublicationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('publications_list')
    else:
        form = PublicationForm()
    return render(request, 'revista/publication_form.html', {'form': form})

def publication_edit(request, pk):
    publication = get_object_or_404(Publication, pk=pk)
    if request.method == 'POST':
        form = PublicationForm(request.POST, instance=publication)
        if form.is_valid():
            form.save()
            return redirect('publications_list')
    else:
        form = PublicationForm(instance=publication)
    return render(request, 'revista/publication_form.html', {'form': form})

def publication_detail(request, pk):
    publication = get_object_or_404(Publication, pk=pk)
    return render(request, 'revista/publication_detail.html', {'publication': publication})


# -----------------------------------------
#  REGISTRO DE USUARIOS
# -----------------------------------------
def user_register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('students_list')
    else:
        form = UserRegisterForm()
    return render(request, 'revista/user_register.html', {'form': form})

from django.db import models

# ----- ESTUDIANTE -----
class Student(models.Model):
    first_name = models.CharField("Nombre", max_length=50)
    last_name = models.CharField("Apellido", max_length=50)
    student_id = models.CharField("Carnet", max_length=20, unique=True)
    email = models.EmailField("Correo")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

# ----- PUBLICADOR -----
class Publisher(models.Model):
    first_name = models.CharField("Nombre", max_length=50)
    last_name = models.CharField("Apellido", max_length=50)
    email = models.EmailField("Correo")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

# ----- AUTORIZADOR -----
class Authorizer(models.Model):
    first_name = models.CharField("Nombre", max_length=50)
    last_name = models.CharField("Apellido", max_length=50)
    email = models.EmailField("Correo")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

# ----- PUBLICACIÓN -----
class Publication(models.Model):
    title = models.CharField("Título", max_length=200)
    content = models.TextField("Contenido")
    date = models.DateField("Fecha de publicación")
    author = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

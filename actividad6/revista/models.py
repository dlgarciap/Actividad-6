from django.db import models
from django.urls import reverse

class Publisher(models.Model):
    first_name = models.CharField("Nombre", max_length=50)
    last_name = models.CharField("Apellido", max_length=50)
    student_id = models.CharField("Carnet", max_length=30, unique=True)
    email = models.EmailField("Email")

    class Meta:
        verbose_name = "Estudiante Publicador"
        verbose_name_plural = "Estudiantes Publicadores"

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.student_id})"

    def get_absolute_url(self):
        return reverse('revista:publisher_detail', kwargs={'pk': self.pk})


class Authorizer(models.Model):
    first_name = models.CharField("Nombre", max_length=50)
    last_name = models.CharField("Apellido", max_length=50)
    student_id = models.CharField("Carnet", max_length=30, unique=True)
    email = models.EmailField("Email")

    class Meta:
        verbose_name = "Estudiante Autorizador"
        verbose_name_plural = "Estudiantes Autorizadores"

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.student_id})"

    def get_absolute_url(self):
        return reverse('revista:authorizer_detail', kwargs={'pk': self.pk})


class Article(models.Model):
    STATUS_CHOICES = (
        ('DR', 'Borrador'),
        ('PB', 'Publicada'),
    )
    title = models.CharField("Título", max_length=200)
    content = models.TextField("Contenido")
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, related_name='articles')
    authorizer = models.ForeignKey(Authorizer, on_delete=models.SET_NULL, null=True, blank=True, related_name='authorized_articles')
    published_at = models.DateTimeField("Fecha publicación", null=True, blank=True)
    status = models.CharField("Estado", max_length=2, choices=STATUS_CHOICES, default='DR')

    class Meta:
        ordering = ['-published_at']
        verbose_name = "Artículo"
        verbose_name_plural = "Artículos"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('revista:article_detail', kwargs={'pk': self.pk})


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    commenter_name = models.CharField("Nombre quien comenta", max_length=150)
    commenter_publisher = models.ForeignKey(Publisher, null=True, blank=True, on_delete=models.SET_NULL)
    text = models.TextField("Comentario")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Comentario"
        verbose_name_plural = "Comentarios"

    def __str__(self):
        return f"Comentario por {self.commenter_name} en {self.article.title}"
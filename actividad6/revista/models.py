from django.db import models
from django.utils.text import slugify
from django.core.exceptions import ValidationError
from django.urls import reverse

class Student(models.Model):
    student_id = models.CharField('Matrícula', max_length=20, unique=True)
    first_name = models.CharField('Nombre', max_length=100)
    last_name = models.CharField('Apellido', max_length=100)
    email = models.EmailField('Correo', blank=True, null=True)
    career = models.CharField('Carrera', max_length=100, blank=True, null=True)
    phone = models.CharField('Teléfono', max_length=20, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Estudiante'
        verbose_name_plural = 'Estudiantes'
        ordering = ['last_name', 'first_name']

    def __str__(self):
        return f"{self.student_id} - {self.first_name} {self.last_name}"


class Publication(models.Model):
    STATUS_CHOICES = (
        ('P','Pendiente'),
        ('A','Autorizada'),
        ('R','Rechazada'),
    )
    title = models.CharField('Título', max_length=255)
    slug = models.SlugField('Slug', max_length=255, unique=True, blank=True)
    content = models.TextField('Contenido')
    publisher = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='published_articles', verbose_name='Publica')
    authorizer = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True, blank=True, related_name='authorized_articles', verbose_name='Autoriza')
    status = models.CharField('Estado', max_length=1, choices=STATUS_CHOICES, default='P')
    published_at = models.DateTimeField('Fecha de publicación', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Publicación'
        verbose_name_plural = 'Publicaciones'
        ordering = ['-created_at']

    def clean(self):
        if self.authorizer and self.authorizer == self.publisher:
            raise ValidationError('El autor y el autorizador no pueden ser la misma persona.')

    def save(self, *args, **kwargs):
        if not self.slug:
            base = slugify(self.title)[:200]
            slug = base
            counter = 1
            while Publication.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug = f"{base}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('revista:publication_detail', args=[self.slug])


class Comment(models.Model):
    publication = models.ForeignKey(Publication, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True, blank=True, related_name='comments')
    content = models.TextField('Comentario')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Comentario'
        verbose_name_plural = 'Comentarios'
        ordering = ['-created_at']

    def __str__(self):
        author = self.author if self.author else "Anónimo"
        return f"Comentario de {author} en {self.publication}"

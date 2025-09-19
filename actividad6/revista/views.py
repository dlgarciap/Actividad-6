from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView
from django.contrib import messages

from .models import Student, Publication, Comment
from .forms import StudentForm, PublicationForm, CommentForm

# STUDENTS
class StudentListView(ListView):
    model = Student
    template_name = 'revista/students_list.html'
    context_object_name = 'students'

class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'revista/student_form.html'
    success_url = reverse_lazy('revista:students_list')

class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'revista/student_form.html'
    success_url = reverse_lazy('revista:students_list')


# PUBLICATIONS
class PublicationListView(ListView):
    model = Publication
    template_name = 'revista/publications_list.html'
    context_object_name = 'publications'
    queryset = Publication.objects.select_related('publisher','authorizer').order_by('-created_at')

class PublicationCreateView(CreateView):
    model = Publication
    form_class = PublicationForm
    template_name = 'revista/publication_form.html'
    success_url = reverse_lazy('revista:publications_list')

class PublicationUpdateView(UpdateView):
    model = Publication
    form_class = PublicationForm
    template_name = 'revista/publication_form.html'
    success_url = reverse_lazy('revista:publications_list')


class PublicationDetailView(DetailView):
    model = Publication
    template_name = 'revista/publication_detail.html'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    context_object_name = 'publication'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        if 'comment_form' not in ctx:
            ctx['comment_form'] = CommentForm()
        ctx['comments'] = self.object.comments.select_related('author').all()
        return ctx

    def post(self, request, *args, **kwargs):
        # procesar envío del formulario de comentario
        self.object = self.get_object()
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.publication = self.object
            comment.save()
            messages.success(request, "Comentario agregado correctamente.")
            return redirect(self.object.get_absolute_url())
        else:
            # renderizar la misma página con errores
            ctx = self.get_context_data(comment_form=form)
            return self.render_to_response(ctx)

from django.views.generic import ListView
from .models import Student, Publication

class PublicationListView(ListView):
    model = Publication
    template_name = 'revista/publications_list.html'
    context_object_name = 'publications'
    queryset = Publication.objects.select_related('publisher','authorizer').order_by('-created_at')

class PublishersListView(ListView):
    model = Student
    template_name = 'revista/publishers_list.html'
    context_object_name = 'publishers'

    def get_queryset(self):
        return Student.objects.filter(published_articles__isnull=False).distinct().order_by('last_name')

class AuthorizersListView(ListView):
    model = Student
    template_name = 'revista/authorizers_list.html'
    context_object_name = 'authorizers'

    def get_queryset(self):
        return Student.objects.filter(authorized_articles__isnull=False).distinct().order_by('last_name')

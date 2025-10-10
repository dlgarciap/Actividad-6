from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Publisher, Authorizer, Article, Comment

# Articles
class ArticleListView(ListView):
    model = Article
    template_name = 'revista/publications_list.html'   # ajusta según tu nombre de template
    context_object_name = 'publications'
    paginate_by = 10

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'revista/publication_detail.html'
    context_object_name = 'publication'

class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    fields = ['title', 'content', 'publisher', 'authorizer', 'status', 'published_at']
    template_name = 'revista/publication_form.html'

class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    model = Article
    fields = ['title', 'content', 'publisher', 'authorizer', 'status', 'published_at']
    template_name = 'revista/publication_form.html'

# Publishers (students)
class PublisherListView(ListView):
    model = Publisher
    template_name = 'revista/publisher_list.html'
    context_object_name = 'publishers'

class PublisherDetailView(DetailView):
    model = Publisher
    template_name = 'revista/publisher_detail.html'
    context_object_name = 'publisher'

class PublisherUpdateView(LoginRequiredMixin, UpdateView):
    model = Publisher
    fields = ['first_name', 'last_name', 'student_id', 'email']
    template_name = 'revista/student_form.html'  # si ya usas student_form.html

# Authorizers
class AuthorizerListView(ListView):
    model = Authorizer
    template_name = 'revista/authorizers_list.html'
    context_object_name = 'authorizers'

class AuthorizerDetailView(DetailView):
    model = Authorizer
    template_name = 'revista/authorizer_detail.html'
    context_object_name = 'authorizer'

class AuthorizerUpdateView(LoginRequiredMixin, UpdateView):
    model = Authorizer
    fields = ['first_name', 'last_name', 'student_id', 'email']
    template_name = 'revista/authorizer_form.html'
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Publisher, Authorizer, Article, Comment

# --- Articles ---
class ArticleListView(ListView):
    model = Article
    template_name = 'revista/article_list.html'
    context_object_name = 'articles'
    paginate_by = 10

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'revista/article_detail.html'
    context_object_name = 'article'

class ArticleCreateView(CreateView):
    model = Article
    fields = ['title', 'content', 'publisher', 'authorizer', 'status', 'published_at']
    template_name = 'revista/article_form.html'

class ArticleUpdateView(UpdateView):
    model = Article
    fields = ['title', 'content', 'publisher', 'authorizer', 'status', 'published_at']
    template_name = 'revista/article_form.html'

# --- Publishers ---
class PublisherListView(ListView):
    model = Publisher
    template_name = 'revista/publisher_list.html'
    context_object_name = 'publishers'

class PublisherDetailView(DetailView):
    model = Publisher
    template_name = 'revista/publisher_detail.html'
    context_object_name = 'publisher'

class PublisherUpdateView(UpdateView):
    model = Publisher
    fields = ['first_name', 'last_name', 'student_id', 'email']
    template_name = 'revista/publisher_form.html'

# --- Authorizers ---
class AuthorizerListView(ListView):
    model = Authorizer
    template_name = 'revista/authorizer_list.html'
    context_object_name = 'authorizers'

class AuthorizerDetailView(DetailView):
    model = Authorizer
    template_name = 'revista/authorizer_detail.html'
    context_object_name = 'authorizer'

class AuthorizerUpdateView(UpdateView):
    model = Authorizer
    fields = ['first_name', 'last_name', 'student_id', 'email']
    template_name = 'revista/authorizer_form.html'
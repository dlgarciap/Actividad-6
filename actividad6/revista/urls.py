from django.urls import path
from . import views

app_name = 'revista'

urlpatterns = [
    # Articles
    path('articles/', views.ArticleListView.as_view(), name='article_list'),
    path('articles/add/', views.ArticleCreateView.as_view(), name='article_add'),
    path('articles/<int:pk>/', views.ArticleDetailView.as_view(), name='article_detail'),
    path('articles/<int:pk>/edit/', views.ArticleUpdateView.as_view(), name='article_edit'),

    # Publishers
    path('publishers/', views.PublisherListView.as_view(), name='publisher_list'),
    path('publishers/<int:pk>/', views.PublisherDetailView.as_view(), name='publisher_detail'),
    path('publishers/<int:pk>/edit/', views.PublisherUpdateView.as_view(), name='publisher_edit'),

    # Authorizers
    path('authorizers/', views.AuthorizerListView.as_view(), name='authorizer_list'),
    path('authorizers/<int:pk>/', views.AuthorizerDetailView.as_view(), name='authorizer_detail'),
    path('authorizers/<int:pk>/edit/', views.AuthorizerUpdateView.as_view(), name='authorizer_edit'),
]

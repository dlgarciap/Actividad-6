from django.urls import path
from .views import (
    PublicationListView, PublicationCreateView, PublicationUpdateView, PublicationDetailView,
    StudentListView, StudentCreateView, StudentUpdateView,
)

app_name = 'revista'

urlpatterns = [
    # publicaciones
    path('publicaciones/', PublicationListView.as_view(), name='publications_list'),
    path('publicaciones/nueva/', PublicationCreateView.as_view(), name='publication_create'),
    path('publicaciones/<slug:slug>/editar/', PublicationUpdateView.as_view(), name='publication_update'),
    path('publicaciones/<slug:slug>/', PublicationDetailView.as_view(), name='publication_detail'),

    # estudiantes (publicadores y autorizadores)
    path('estudiantes/', StudentListView.as_view(), name='students_list'),
    path('estudiantes/nuevo/', StudentCreateView.as_view(), name='student_create'),
    path('estudiantes/<int:pk>/editar/', StudentUpdateView.as_view(), name='student_update'),
]

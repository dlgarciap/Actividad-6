from django.urls import path
from . import views

urlpatterns = [
    # --- ESTUDIANTES ---
    path('students/', views.students_list, name='students_list'),
    path('students/add/', views.student_create, name='student_create'),
    path('students/<int:pk>/edit/', views.student_edit, name='student_edit'),
    path('students/<int:pk>/', views.student_detail, name='student_detail'),

    # --- PUBLICADORES ---
    path('publishers/', views.publishers_list, name='publishers_list'),
    path('publishers/add/', views.publisher_create, name='publisher_create'),
    path('publishers/<int:pk>/edit/', views.publisher_edit, name='publisher_edit'),
    path('publishers/<int:pk>/', views.publisher_detail, name='publisher_detail'),

    # --- AUTORIZADORES ---
    path('authorizers/', views.authorizers_list, name='authorizers_list'),
    path('authorizers/add/', views.authorizer_create, name='authorizer_create'),
    path('authorizers/<int:pk>/edit/', views.authorizer_edit, name='authorizer_edit'),
    path('authorizers/<int:pk>/', views.authorizer_detail, name='authorizer_detail'),

    # --- PUBLICACIONES ---
    path('publications/', views.publications_list, name='publications_list'),
    path('publications/add/', views.publication_create, name='publication_create'),
    path('publications/<int:pk>/edit/', views.publication_edit, name='publication_edit'),
    path('publications/<int:pk>/', views.publication_detail, name='publication_detail'),

    # --- USUARIOS ---
    path('users/add/', views.user_register, name='user_register'),
]

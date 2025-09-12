from django.urls import path
from .views import PublicationListView, PublishersListView, AuthorizersListView

app_name = 'revista'

urlpatterns = [
    path('publicaciones/', PublicationListView.as_view(), name='publications_list'),
    path('publicaciones/publicadores/', PublishersListView.as_view(), name='publishers_list'),
    path('publicaciones/autorizadores/', AuthorizersListView.as_view(), name='authorizers_list'),
]

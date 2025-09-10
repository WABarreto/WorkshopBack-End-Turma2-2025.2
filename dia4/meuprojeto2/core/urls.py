from django.urls import path
from .views import EnderecoDeleteView, EnderecoListView, EnderecoDetailView, HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('list/', EnderecoListView.as_view(), name = 'list'),
    path('delete/<int:pk>/', EnderecoDeleteView.as_view(), name = 'delete'),
    path('detail/<int:pk>/', EnderecoDetailView.as_view(), name = 'detail')
]
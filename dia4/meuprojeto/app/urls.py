from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('app/', views.renderizar_tela_do_app, name='app2')
]
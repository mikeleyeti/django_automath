from django.urls import path

from . import views

urlpatterns = [
    path('', views.get_config, name='index'),
    path('<titre>/', views.detail, name='detail'),
]
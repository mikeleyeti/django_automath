from django.conf.urls import url
from django.urls import path

from . import views

app_name = "automath"
urlpatterns = [
    url('^$', views.get_config , name='index'),
    path('<titre>/', views.detail, name='detail')
]
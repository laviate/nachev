from django.urls import path
from statics import views

app_name = 'statics'
urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
]

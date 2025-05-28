from django.urls import path
from . import views

urlpatterns = [
    path('', views.create_profile, name='create_profile'),
    path('profiles/', views.profiles_list, name='profiles_list'),
]
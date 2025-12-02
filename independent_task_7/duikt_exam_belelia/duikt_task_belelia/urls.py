from django.urls import path
from . import views

urlpatterns = [
    path("install/", views.install),
    path("duikt_page_belelia/", views.cars_page),
]

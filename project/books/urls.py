from django.urls import path
from . import views

urlpatterns = [
    path("", views.salom, name="salom"),
    path("salom/", views.salom, name="salom_alt"),
]

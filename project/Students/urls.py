from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_list, name='student_list'),
    path('add/', views.student_add, name='add_student'),
    path('create/', views.student_add, name='create-student'),
    path('redirect/', views.student_redirect, name='student_redirect'),
    path('<int:student_id>/', views.student_detail, name='student_detail'),
    path('<int:student_id>/edit/', views.student_edit, name='student_edit'),
]

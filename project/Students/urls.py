from django.urls import path
from . import views


urlpatterns = [
    path('', views.student_list, name='student_list'),
    path('redirect/', views.student_redirect, name='student_redirect'),
    path('<int:student_id>/', views.student_detail, name='student_detail'),
]

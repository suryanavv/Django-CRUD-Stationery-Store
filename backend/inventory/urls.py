from django.urls import path
from . import views

urlpatterns = [
    path('', views.stationery_list, name='stationery_list'),
    path('<int:pk>/', views.stationery_detail, name='stationery_detail'),
    path('new/', views.stationery_create, name='stationery_create'),
    path('<int:pk>/edit/', views.stationery_update, name='stationery_update'),
    path('<int:pk>/delete/', views.stationery_delete, name='stationery_delete'),
]

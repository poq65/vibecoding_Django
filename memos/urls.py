from django.urls import path
from . import views

urlpatterns = [
    path('', views.memo_list, name='home'),
    path('memo/new/', views.memo_create, name='memo_create'),
    path('memo/<int:pk>/', views.memo_detail, name='memo_detail'),
    path('memo/<int:pk>/edit/', views.memo_update, name='memo_update'),
    path('memo/<int:pk>/delete/', views.memo_delete, name='memo_delete'),
]
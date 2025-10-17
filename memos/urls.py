from django.urls import path
from . import views

urlpatterns = [
    path('', views.memo_list, name='home'),
]
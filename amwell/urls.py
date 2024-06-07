
from django.urls import path 

from .  import views

urlpatterns = [
    path('create/', views.CustomUser_create, name='CustomUser_create'),
    # path('<int:pk>/update/', views.CustomUser_update, name='CustomUser_update'),
    # path('<int:pk>/delete/', views.CustomUser_delete, name='CustomUser_delete'),
     
]
# importing paths
from django.urls import path

# importing views
from . import views

urlpatterns = [
    path('task_list/', views.task_list, name = 'task_list'),
    path('add/', views.add_task, name = 'add_task'),
    path('complete/<int:task_id>/', views.complete_task, name = 'complete_task'),
    path('delete/<int:task_id>/', views.delete_task, name = 'delete_task'),

]
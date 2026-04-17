from django.urls import path
from . import views

urlpatterns = [
    path('add_task/', views.add_tasks, name = 'add_task'),
    # path('contact_us/', views.contact_us, name='contact_us'),
    path('contact_us/', views.contact_us_02, name='contact_us_02'),
    path('add_tags/', views.add_tags, name='add_tags'),
    path('delete_tag/<int:tag_id>/', views.delete_tag, name='delete_tag'),
    path('home/', views.home, name = 'home'),
    path('about/',views.about, name='about'),
    path('complete_task/<int:task_id>/', views.complete_task, name = 'complete_task'),
    path('delete_task/<int:task_id>/', views.delete_task, name='delete_task')
]
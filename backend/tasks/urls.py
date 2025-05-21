from django.urls import path
from . import views

app_name = 'tasks'

urlpatterns = [
    path('', views.task_list, name='task-list'),
    path('add/', views.add_task, name='add-task'),
    path('<int:task_id>/', views.task_detail, name='task-detail'),
    path('<int:task_id>/edit/', views.edit_task, name='edit-task'),
    path('<int:task_id>/delete/', views.delete_task, name='delete-task'),
    # path('<int:task_id>/remove-employee/', views.remove_employee_from_task, name='remove-employee'), 
]

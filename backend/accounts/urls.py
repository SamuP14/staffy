from django.urls import path

from . import views

app_name = 'accounts'

urlpatterns = [
    path('profile/', views.profile_list, name='profile-list'),
    path('profile/add/', views.add_profile, name='add-profile'),
    path('profile/<str:username>/', views.profile_detail, name='profile-detail'),
    path('profile/<str:username>/edit/', views.edit_profile, name='edit-profile'),
    path('profile/<str:username>/delete/', views.delete_profile, name='delete-profile'),
    path('profile/<str:username>/role/add/', views.profile_add_role, name='profile-add-role'),
    path('profile/<str:username>/role/<str:role_code>/delete/', views.profile_delete_role, name='profile-delete-role'),

    path('role/', views.role_list, name='role-list'),
    path('role/add/', views.add_role, name='role-add'),
    path('role/<str:role_code>/delete/', views.delete_role, name='role-delete'),

    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
] 
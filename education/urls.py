from django.urls import path

from education import views

app_name='education'

urlpatterns = [
    path('', views.home, name='home'),

    # ------------ (CREATE URLS) ------------ #
    path('create_lesson/', views.createLesson, name="create_lesson"),
    path('create_topic/', views.createTopic, name="create_topic"),
    path('create_organization/', views.createOrganization, name="create_organization"),
    path('create_human/', views.createHuman, name="create_human"),

    # ------------ (UPDATE URLS) ------------ # 
    path('update_lesson/<str:pk>/', views.updateLesson, name="update_lesson"),
    path('update_topic/<str:pk>/', views.updateTopic, name="update_topic"),
    path('update_organization/<str:pk>/', views.updateOrganization, name="update_organization"),
    path('update_human/<str:pk>/', views.updateHuman, name="update_human"),

    # ------------ (DELETE URLS) ------------ # 
    path('delete_lesson/<str:pk>/', views.deleteLesson, name="delete_lesson"),
    path('delete_topic/<str:pk>/', views.deleteTopic, name="delete_topic"),
    path('delete_organization/<str:pk>/', views.deleteOrganization, name="delete_organization"),
    path('delete_human/<str:pk>/', views.deleteHuman, name="delete_human"),

]
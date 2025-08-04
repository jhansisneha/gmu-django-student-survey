from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('survey/', views.create_survey, name='create_survey'),
    path('surveys/', views.list_surveys, name='list_surveys'),
    path('survey/update/<int:id>/', views.update_survey, name='update_survey'),
    #path('survey/update/<int:survey_id>/', views.update_survey, name='update_survey'),
    path('survey/delete/<int:id>/', views.delete_survey, name='delete_survey'),
]
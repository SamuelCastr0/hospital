from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('create-patient/', views.CreatePatientView.as_view(), name='create-patient'),
    path('add-existent-patient/', views.AddExistentPatient.as_view(), name='add-existent-patient'),
    path('register-symptoms/<int:pk>/', views.RegisterSymptomsView.as_view(), name='register-symptoms'),
    path('create-symptom/<int:pk>/', views.CreateSymptom.as_view(), name='create-symptom'),
    path('generate-diagnostic/<int:pk>/', views.GenerateDiagnosticView.as_view(), name='generate-diagnostic'),
]

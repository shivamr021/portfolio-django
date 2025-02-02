from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('skills/', views.skills, name='skills'),
    path('certifications/', views.certifications, name='certifications'),
    path('project/', views.project, name='project'),
    path('experience/', views.experience, name='experience'),
    path('assignments/', views.assignments, name='assignments'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.team_list, name='team-list'),
    path('management/', views.team_detail, {'team_name': 'management'}, name='management'),
    path('procurement/', views.team_detail, {'team_name': 'procurement'}, name='procurement'),
    # Add similar paths for other teams
]

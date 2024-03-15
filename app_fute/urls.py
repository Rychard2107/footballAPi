from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('matches/<int:competition_id>/', views.match_list, name='match_list'),
    path('teams/<int:competition_id>', views.team_list, name='team_list'),
    path('team/<int:team_id>', views.team, name='team'),
]

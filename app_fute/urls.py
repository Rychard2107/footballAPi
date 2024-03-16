from django.urls import path
from . import views
from .views import CompetitionCreateView, TeamCreateView, MatchCreateView

urlpatterns = [
    path('', views.home, name='home'),
    # api paths
    path('matches/<int:competition_id>/', views.match_list, name='match_list'),
    path('teams/<int:competition_id>', views.team_list, name='team_list'),
    path('team/<int:team_id>', views.team, name='team'),
    # creation paths
    path('competition/create/', CompetitionCreateView.as_view(), name='competition_create'), # noqa
    path('team/create/', TeamCreateView.as_view(), name='team_create'),
    path('match/create/', MatchCreateView.as_view(), name='match_create'),
    path('matches/', views.view_created_matches, name='created_matches'),
]

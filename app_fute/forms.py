from django import forms
from .models import Competition, Team, Match


class CompetitionForm(forms.ModelForm):
    class Meta:
        model = Competition
        fields = ['name']


class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        exclude = ['founded']
        fields = ['name',
                  'tla',
                  'area',]


class MatchForm(forms.ModelForm):
    class Meta:
        model = Match
        fields = ['competition',
                  'home_team',
                  'away_team',
                  'match_date',
                  'home_team_score',
                  'away_team_score']

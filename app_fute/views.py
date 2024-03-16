from django.shortcuts import render
import requests
from django.core.paginator import Paginator
from datetime import datetime
from django.views.generic.edit import CreateView
from .models import Competition, Team, Match
from .forms import CompetitionForm, TeamForm, MatchForm


def home(request):
    try:
        url = 'https://api.football-data.org/v4/competitions/'
        headers = {'X-Auth-Token': '02dbfc8a7b1f4f6f9bd8817070cce254'}
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()

        competitions = []

        for competition in data['competitions']:
            name = competition['name']
            id = competition['id']

            competitions.append({'name': name, 'id': id})

        return render(request, 'app_fute/pages/home.html', {'competitions': competitions}) # noqa
    except requests.exceptions.RequestException as e:
        # Erro de requisição
        error_message = f"Seu erro foi amar demais, e mais esse aqui também: {str(e)}" # noqa

        return render(request, 'app_fute/pages/error.html', {'error_message': error_message}) # noqa
    except Exception as e:
        # Erros gerais
        error_message = f"Este erro foi inesperado: {str(e)}"

        return render(request, 'app_fute/pages/error.html', {'error_message': error_message}) # noqa


def match_list(request, competition_id):
    try:
        url = f'https://api.football-data.org/v4/competitions/{competition_id}/matches' # noqa
        headers = {'X-Auth-Token': '02dbfc8a7b1f4f6f9bd8817070cce254'}
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()

        matches = []

        for match in data['matches']:
            home_team_name = match['homeTeam']['name']
            away_team_name = match['awayTeam']['name']
            home_team_id = match['homeTeam']['id']
            away_team_id = match['awayTeam']['id']
            match_date = datetime.strptime(match['utcDate'], '%Y-%m-%dT%H:%M:%SZ').strftime('%d/%m/%Y') # noqa
            match_score_home = match['score']['fullTime']['home']
            match_score_away = match['score']['fullTime']['away']

            matches.append({'home_team_name':  home_team_name,
                            'away_team_name': away_team_name,
                            'home_team_id': home_team_id,
                            'away_team_id': away_team_id,
                            'match_date': match_date,
                            'match_score_home': match_score_home,
                            'match_score_away': match_score_away})

        matches_paginator = Paginator(matches, 30)
        page_num = request.GET.get('page')
        page = matches_paginator.get_page(page_num)
        return render(request, 'app_fute/pages/match_list.html', {'competition_id': competition_id , 'page': page}) # noqa

    except Exception as e:
        # Erros de partida
        error_message = f"Erro ao listar as partidas: {str(e)}"
        return render(request, 'app_fute/pages/error.html', {'error_message': error_message}) # noqa


def team_list(request, competition_id):
    try:
        url = f'https://api.football-data.org/v4/competitions/{competition_id}/teams' # noqa
        headers = {'X-Auth-Token': '02dbfc8a7b1f4f6f9bd8817070cce254'}
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()

        teams = []
        for team in data['teams']:
            team_id = team['id']
            team_name = team['name']
            sigla = team['tla']
            area = team['area']['name']
            founded = team['founded']

            teams.append({'team_id': team_id,
                          'team_name': team_name,
                          'sigla': sigla,
                          'area': area,
                          'founded': founded})

        teams_paginator = Paginator(teams, 30)
        page_num = request.GET.get('page')
        page = teams_paginator.get_page(page_num)
        return render(request, 'app_fute/pages/team_list.html', {'competition_id': competition_id , 'page': page}) # noqa

    except Exception as e:
        # Erros de times
        error_message = f"Erro ao listar os times: {str(e)}"
        return render(request, 'app_fute/pages/error.html', {'error_message': error_message}) # noqa


def team(request, team_id):
    try:
        url = f'https://api.football-data.org/v4/teams/{team_id}' # noqa
        headers = {'X-Auth-Token': '02dbfc8a7b1f4f6f9bd8817070cce254'}
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()

        team_name = data['name']
        squad = []
        for player in data['squad']:
            player_name = player['name']
            position = player['position']

            squad.append({'player_name': player_name,
                          'position': position,
                          })

        return render(request, 'app_fute/pages/team.html', {'team_id': team_id ,'team_name': team_name , 'squad': squad}) # noqa

    except Exception as e:
        # Erros de time
        error_message = f"Erro ao requisitar o time: {str(e)}"
        return render(request, 'app_fute/pages/error.html', {'error_message': error_message}) # noqa


class CompetitionCreateView(CreateView):
    model = Competition
    form_class = CompetitionForm
    template_name = 'app_fute/pages/competition_form.html'
    success_url = '/'


class TeamCreateView(CreateView):
    model = Team
    form_class = TeamForm
    template_name = 'app_fute/pages/team_form.html'
    success_url = '/'


class MatchCreateView(CreateView):
    model = Match
    form_class = MatchForm
    template_name = 'app_fute/pages/match_form.html'
    success_url = '/'


def view_created_matches(request):
    matches = Match.objects.all()  # Obtém todas as partidas criadas
    return render(request, 'app_fute/pages/created_matches.html', {'matches': matches}) # noqa

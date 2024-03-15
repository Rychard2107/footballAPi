from django.shortcuts import render
import requests
from django.core.paginator import Paginator
from datetime import datetime

# from .models import Competition


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
            match_date = datetime.strptime(match['utcDate'], '%Y-%m-%dT%H:%M:%SZ').strftime('%d/%m/%Y')
            match_score_home = match['score']['fullTime']['home']
            match_score_away = match['score']['fullTime']['away']

            matches.append({'home_team_name':  home_team_name,
                            'away_team_name': away_team_name,
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

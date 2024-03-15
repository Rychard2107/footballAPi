from django.shortcuts import render
import requests
# from .models import Competition


def home(request):
    try:
        url = 'https://api.football-data.org/v4/competitions/'
        headers = {'X-Auth-Token': '02dbfc8a7b1f4f6f9bd8817070cce254'}
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        return render(request, 'app_fute/pages/home.html', {'data': data})
    except requests.exceptions.RequestException as e:
        error_message = f"Seu erro foi amar demais, e mais esse aqui também: {str(e)}"
        return render(request, 'app_fute/pages/error.html', {'error_message': error_message})
    except Exception as e:
        # Erros gerais
        error_message = f"Este erro foi inesperado: {str(e)}"
        return render(request, 'app_fute/pages/error.html', {'error_message': error_message})

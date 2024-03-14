import requests


url = 'https://api.football-data.org/v4/teams/'
headers = {'X-Auth-Token': '02dbfc8a7b1f4f6f9bd8817070cce254'}

response = requests.get(url, headers=headers)
for Teams in response.json()['teams']:
    print(Teams)

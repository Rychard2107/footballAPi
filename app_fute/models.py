from django.db import models


class Competition(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=50, unique=True)
    tla = models.CharField(max_length=3)
    area = models.CharField(max_length=30)
    founded = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Match(models.Model):
    competition = models.ForeignKey(Competition, on_delete=models.CASCADE)
    home_team = models.ForeignKey(Team, related_name='home_matches', on_delete=models.CASCADE) # noqa
    away_team = models.ForeignKey(Team, related_name='away_matches', on_delete=models.CASCADE) # noqa
    match_date = models.DateField()
    home_team_score = models.IntegerField()
    away_team_score = models.IntegerField()

    def __str__(self):
        return f"{self.home_team} vs {self.away_team}"

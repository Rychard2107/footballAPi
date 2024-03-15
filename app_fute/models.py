""" from django.db import models


class Competition(models.Model):
    name = models.CharField(max_length=30)
    match = models.ForeignKey('Match')

    def __str__(self):
        return self.name


class Match(models.Model):
    name = models.CharField(max_length=30)
    team = models.ManyToManyField('Team', related_name='teams')

    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
 """
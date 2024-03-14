from django.db import models


class Times(models.Model):
    nome_time = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

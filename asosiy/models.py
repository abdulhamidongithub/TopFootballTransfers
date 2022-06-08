from django.db import models
from django.conf import settings

class Club(models.Model):
    name = models.CharField(max_length=100)
    logo = models.FileField(upload_to="rasmlar/", blank=True, null=True)
    country = models.CharField(max_length=100, blank=True)
    president = models.CharField(max_length=100, blank=True)
    coach = models.CharField(max_length=100, blank=True)
    stadium = models.CharField(max_length=100, blank=True)
    foundation = models.DateField(null=True, blank=True)
    record_arrival = models.CharField(max_length=300)
    record_departure = models.CharField(max_length=300)

    def __str__(self):
        return self.name

class Player(models.Model):
    name = models.CharField(max_length=100)
    nationality = models.CharField(max_length=100, blank=True)
    position = models.CharField(max_length=100, blank=True)
    club = models.ForeignKey(Club, on_delete=models.SET_NULL, null=True)
    value = models.IntegerField()

    def __str__(self):
        return self.name

class U_20(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    club = models.ForeignKey(Club, on_delete=models.SET_NULL, null=True)
    value = models.IntegerField()

    def __str__(self):
        return self.name

class Transfer(models.Model):
    player = models.ForeignKey(Player, on_delete=models.SET_NULL, null=True)
    old_club = models.CharField(max_length=100, blank=True, null=True)
    new_club = models.CharField(max_length=100, blank=True, null=True)
    value = models.IntegerField()
    value_by_tft = models.IntegerField()
    season = models.CharField(max_length=100, blank=True, null=True)

class Expenditure_Records(models.Model):
    club = models.CharField(max_length=100)
    season = models.CharField(max_length=30)
    expenditure = models.IntegerField()

class Income_Records(models.Model):
    club = models.CharField(max_length=100)
    season = models.CharField(max_length=30)
    income = models.IntegerField()

class Predictions(models.Model):
    player = models.CharField(max_length=100)
    old_club = models.CharField(max_length=100)
    new_club = models.CharField(max_length=100)
    value = models.FloatField()
    value_by_tft = models.FloatField()
    divergence = models.IntegerField()



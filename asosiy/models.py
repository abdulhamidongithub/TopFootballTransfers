from django.db import models

class Club(models.Model):
    name = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    logo = models.FileField(null=True, blank=True)
    prezident = models.CharField(max_length=100, blank=True, null=True)
    murabbiy = models.CharField(max_length=100, blank=True, null=True)
    foundation = models.DateField(null=True, blank=True)
    eng_katta_tr = models.CharField(max_length=100, blank=True, null=True)
    eng_katta_sotuv = models.CharField(max_length=100, blank=True, null=True)
    def __str__(self):
        return self.name

class Player(models.Model):
    name = models.CharField(max_length=50)
    position = models.CharField(max_length=30)
    nationality = models.CharField(max_length=30)
    birth_date = models.DateField(null=True, blank=True)
    value = models.FloatField()
    club = models.ForeignKey(Club, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.name

class Transfer(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE, null=True)
    old_club = models.ForeignKey(Club, on_delete=models.CASCADE, related_name="sotganlari", null=True)
    new_club = models.ForeignKey(Club, on_delete=models.CASCADE, null=True)
    value = models.FloatField()
    tax_narx = models.FloatField(null=True, blank=True)
    season = models.CharField(max_length=7, null=True, blank=True)


class HozirgiMavsum(models.Model):
    mavsum = models.CharField(max_length=7)
    def __str__(self):
        return self.mavsum

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



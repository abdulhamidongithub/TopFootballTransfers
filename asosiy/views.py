from django.db.models import Count, Sum
from django.shortcuts import render
from django.views import View
from .models import *

class Home(View):
    def get(self, request):
        return render(request, "index.html")

class About(View):
    def get(self, request):
        return render(request, "about.html")

class Tryouts(View):
    def get(self, request):
        return render(request, "tryouts.html")

class ClubsView(View):
    def get(self, request):
        data = {
            "clubs" : Club.objects.annotate(qiymatlar=Sum('players__value')).order_by("-qiymatlar")
        }
        return render(request, "clubs.html", data)

class PlayersView(View):
    def get(self, request):
        data = {
            "players": Player.objects.all().order_by("-value")
        }
        return render(request, "players.html", data)

class TransfersView(View):
    def get(self, request):
        h_mavsum = HozirgiMavsum.objects.last().mavsum
        data = {
            "transfers" : Transfer.objects.filter(season=h_mavsum).order_by("season", "-value")
        }
        return render(request, "latest-transfers.html", data)

class U20PlayersView(View):
    def get(self, request):
        from datetime import date, timedelta
        enddate = date.today()
        startdate = enddate - timedelta(days=7305)
        data = {
            "players": Player.objects.filter(birth_date__range=[startdate, enddate]).order_by("-value", '-birth_date'),
            "bu_yil": enddate.year
        }
        return render(request, "U-20 players.html", data)

class CountryView(View):
    def get(self, request, country_name):
        if country_name != "other":
            data = {
                "clubs": Club.objects.filter(country=country_name),
                "country":country_name
            }
        else:
            data = {
                "clubs": Club.objects.filter(country=""),
                "country": "Other"
            }
        return render(request, "country.html", data)

class ClubPlayersView(View):
    def get(self, request, club_name):
        cl = Club.objects.get(name=club_name)
        data = {
            "club":cl,
            "players" : Player.objects.filter(club=cl).order_by("-value")
        }
        return render(request, "country-clubs.html", data)

class CourseView(View):
    def get(self, request):
        return render(request, "courses.html")

class TransferArchive(View):
    def get(self, request):
        h_mavsum = HozirgiMavsum.objects.last().mavsum
        data = {
            "seasons" : Transfer.objects.filter(season__lt=h_mavsum).values('season').distinct()
        }
        return render(request, "transfer-archive.html", data)

class SeasonView(View):
    def get(self, request, season):
        data = {
            "transfers" : Transfer.objects.filter(season=season[12:17]),
            "season" : season[12:17]
        }
        return render(request, "season.html", data)



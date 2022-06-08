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
            "clubs" : Club.objects.all()
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
        data = {
            "transfers" : Transfer.objects.all().order_by("season")
        }
        return render(request, "latest-transfers.html", data)

class U20PlayersView(View):
    def get(self, request):
        data = {
            "players": U_20.objects.all().order_by("-value")
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
                "country": ""
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


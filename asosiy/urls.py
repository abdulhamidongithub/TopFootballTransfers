from django.urls import path
from .views import *

urlpatterns = [
    path('', Home.as_view(), name="home"),
    path('about/', About.as_view(), name="about"),
    path('tryouts/', Tryouts.as_view(), name="tryouts"),
    path('clubs/', ClubsView.as_view(), name="clubs"),
    path('countries/<str:country_name>/', CountryView.as_view(), name="countries"),
    path('players/', PlayersView.as_view(), name="players"),
    path('courses/', CourseView.as_view(), name="courses"),
    path('U20-players/', U20PlayersView.as_view(), name="U20-players"),
    path('latest-transfers/', TransfersView.as_view(), name="transfers"),
    path('season/<str:season>/', SeasonView.as_view(), name="season"),
    path('transfer-archive/', TransferArchive.as_view(), name="transfer-archive"),
    path('club_players/<str:club_name>/', ClubPlayersView.as_view(), name="club_players"),
]


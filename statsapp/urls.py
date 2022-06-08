from django.urls import path
from .views import *

urlpatterns = [
    path('', StatsView.as_view(), name="stats"),
    path('top-clubs-by-income/', IncomeView.as_view(), name="income"),
    path('predictions/', PredictionsView.as_view(), name="predictions"),
    path('record_transfers/', RecordTransfersView.as_view(), name="records"),
    path('top-clubs-by-expenditure/', ExpenditureView.as_view(), name="expenditure"),
]

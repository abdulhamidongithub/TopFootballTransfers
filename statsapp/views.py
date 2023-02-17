from django.shortcuts import render
from django.views import View
from asosiy.models import Transfer, Predictions, Expenditure_Records, Income_Records

class StatsView(View):
    def get(self, request):
        return render(request, "stats.html")

class ExpenditureView(View):
    def get(self, request):
        data = {
            "expenditures":Expenditure_Records.objects.all().order_by("expenditure")[:50]
        }
        return render(request, "top-50-clubs-by-expenditure-in-2021.html", data)

class IncomeView(View):
    def get(self, request):
        data = {
            "income": Income_Records.objects.all().order_by("income")[:50]
        }
        return render(request, "top-50-clubs-by-income-in-2021.html", data)

class RecordTransfersView(View):
    def get(self, request):
        data = {
            "transfers":Transfer.objects.filter(value__gt=49.9).order_by("-value")[:150]
        }
        return render(request, "transfer-records.html", data)

class PredictionsView(View):
    def get(self, request):
        data = {
            "predictions": Predictions.objects.all().order_by("divergence", "-value")[:150]
        }
        return render(request, "150-accurate-predictions.html", data)



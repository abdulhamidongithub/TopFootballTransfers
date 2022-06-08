from django.contrib import admin
from .models import *

@admin.register(Club)
class ClubAdmin(admin.ModelAdmin):
    search_fields = ("name", "country",)
    list_filter = ("country",)

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    search_fields = ("name", "club",)
    list_filter = ("club",)

@admin.register(U_20)
class U_20Admin(admin.ModelAdmin):
    search_fields = ("name", "club",)
    list_filter = ("club",)

@admin.register(Transfer)
class TransferAdmin(admin.ModelAdmin):
    search_fields = ("season", "from", "to",)
    list_display = ("player", "old_club", "new_club", "value", "season",)

@admin.register(Expenditure_Records)
class ExpenseAdmin(admin.ModelAdmin):
    search_fields = ("season", "club",)
    list_display = ("season", "club", "expenditure",)

@admin.register(Income_Records)
class IncomeAdmin(admin.ModelAdmin):
    search_fields = ("season", "club",)
    list_display = ("season", "club", "income",)

@admin.register(Predictions)
class PredictionsAdmin(admin.ModelAdmin):
    search_fields = ("player", "old_club","new_club",)
    list_display = ["player", "old_club","new_club","value", "value_by_tft"]

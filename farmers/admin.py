from django.contrib import admin
from .models import Farmer, FarmerLoan, Payment

@admin.register(FarmerLoan)
class FarmerLoanAdmin(admin.ModelAdmin):
    list_display = ['farmer','date_released','total_value','status']

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['loan','farmer','date_paid','amount_paid','balance']

@admin.register(Farmer)
class FarmerAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name','municipality', 'status']
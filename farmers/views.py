from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from farmers.models import Farmer, FarmerLoan, Payment


def home(request):
    return render(request, 'farmers/home.html')

@login_required
def dashboard(request):
    context = {
        'total_farmers': Farmer.objects.count(),
        'active_farmers': Farmer.objects.filter(status='active').count(),
        'total_loans': FarmerLoan.objects.count(),
        'inactive_farmers': Farmer.objects.filter(status='inactive').count(),
        'ongoing_loans': FarmerLoan.objects.filter(status='ongoing').count(),
        'total_payments': Payment.objects.count(),
        'recent_loans': FarmerLoan.objects.order_by('-date_released')[:5],
        'recent_payments': Payment.objects.order_by('-date_paid')[:5],
    }
    return render(request, 'farmers/dashboard.html', context)
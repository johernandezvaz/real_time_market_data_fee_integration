# market_data/views.py
from django.shortcuts import render
from .models import MarketData

def market_data_list(request):
    # Fetch all market data from the database
    market_data_list = MarketData.objects.all()

    return render(request, 'index.html', {
        'market_data_list': market_data_list,
    })

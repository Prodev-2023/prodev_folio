from django.shortcuts import render


# Create your views here.

def portfolioHome(request):
    return render(request, 'portfolio/portfolio_home.html')


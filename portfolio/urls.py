from django.urls import path
from portfolio import views


urlpatterns = [
    path('', views.portfolioHome, name='portfolio_home_page'),
]

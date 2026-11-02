from django.urls import path
from .views import PortfolioView, ContactView

urlpatterns = [
    path("portfolio/", PortfolioView.as_view()),
    path("contact/", ContactView.as_view()),
]

from django.urls import path
from .views import landingView,homeView

urlpatterns = [
        path('', landingView,name='landing'),
        path('home/',homeView, name='home'),
]
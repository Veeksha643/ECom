from django.urls import path
from .views import landingView,homeView,aboutUsView,contactUsView

urlpatterns = [
        path('', landingView,name='landing'),
        path('home/',homeView, name='home'),
        path('aboutus/',aboutUsView,name='about-us'),
        path('contactus/',contactUsView,name='contact-us'),

]
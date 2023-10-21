from django.shortcuts import render

def homeView(request):
    return render (request,'pages/home.html',{})
def landingView(request):
    return render (request,'pages/landing-page.html',{})

# Create your views here.

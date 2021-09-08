from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'portfolio/home.html')

def aboutme(request):
    return render(request, 'portfolio/aboutme.html')

def experiences(request):
    return render(request, 'portfolio/experiences.html')
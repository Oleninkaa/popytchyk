from django.shortcuts import render
from trips.models import Trip

def index(request):
    return render(request, 'index.html')

def user(request):
    context = {}
    trips = Trip.objects.all()
    context['trips'] = trips
    context['title'] = "user page"
    return render(request, 'user.html', context)

def admin(request):
    context = {}
    trips = Trip.objects.all()
    context['trips'] = trips
    context['title'] = "admin page"
    return render(request, 'admin.html', context)

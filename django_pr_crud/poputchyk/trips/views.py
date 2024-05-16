from django.shortcuts import render
from trips.models import Trip
from trips.forms import TripForm, TripForm_xs

def index(request):
    return render(request, 'index.html')

def user(request):
    context = {}
    form = TripForm_xs()
    trips = Trip.objects.all()
    context['trips'] = trips
    context['title'] = "user page"
    if request.method == 'POST':
        if 'save' in request.POST:
            form = TripForm_xs(request.POST)
            form.save()
       
    context['form'] = form
    return render(request, 'user.html', context)





def admin(request):
    context = {}
    form = TripForm()
    trips = Trip.objects.all()
    context['trips'] = trips
    context['title'] = "admin page"
    if request.method == 'POST':
        if 'save' in request.POST:
            pk = request.POST.get('save')
            if not pk:
                form = TripForm(request.POST)
            else:
                trip = Trip.objects.get(id = pk)
                form = TripForm(request.POST, instance = trip)
            form.save()
            form = TripForm()
        elif 'delete' in request.POST:
            pk = request.POST.get('delete')
            trip = Trip.objects.get(id = pk)
            trip.delete()

        elif 'edit' in request.POST:
            pk = request.POST.get('edit')
            trip = Trip.objects.get(id = pk)
            form = TripForm(instance = trip)
    context['form'] = form
    return render(request, 'admin.html', context)

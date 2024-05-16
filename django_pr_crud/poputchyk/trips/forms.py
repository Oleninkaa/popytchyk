from django import forms
from trips.models import Trip


class TripForm(forms.ModelForm):
    class Meta:
        model = Trip
        fields = [ 'name', 'surname', 'start', 'finish', 'date', 'phone', 'email' ]

class TripForm_xs(forms.ModelForm):
    class Meta:
        model = Trip
        fields = [ 'name', 'start', 'finish', 'date']

        
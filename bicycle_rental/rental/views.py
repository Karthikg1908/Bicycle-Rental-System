from django.shortcuts import render
from .models import Bicycle

def home(request):
    bikes = Bicycle.objects.all()

    context = {
        'bikes': bikes
    }

    return render(request, 'home.html', context)
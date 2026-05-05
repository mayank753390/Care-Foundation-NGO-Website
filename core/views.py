from django.shortcuts import render

# Create your views here.
# core/views.py
from django.shortcuts import render
from .models import Activity

def home(request):
    return render(request, 'home.html')
    #return render(request, 'core/home.html')


def about(request):
    return render(request, 'about.html')

def mission_vision(request):
    return render(request, 'mission_vision.html')

def activities(request):
    acts = Activity.objects.all()
    return render(request, 'activities.html', {'activities': acts})

def donate(request):
    return render(request, 'donate.html')

def contact(request):
    return render(request, 'contact.html')

from django.shortcuts import redirect
from django.contrib import messages
from .models import Donation

def process_donation(request):
    if request.method == 'POST':
        amount = request.POST.get('amount')
        citizenship = request.POST.get('citizenship')
        frequency = request.POST.get('frequency', 'Give Once')
        
        if amount and amount.isdigit():
            Donation.objects.create(
                citizenship=citizenship,
                frequency=frequency,
                amount=int(amount)
            )
            messages.success(request, 'Thank you for your generous pledge!')
        else:
            messages.error(request, 'Please enter a valid amount.')
            
    return redirect('home')

def charity_to_poor(request):
    return render(request, 'charity_to_poor.html')


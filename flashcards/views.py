from django.shortcuts import render
from django.http import HttpResponse

cards = [
    {
        'front': 'Front 1',
        'back': 'Back 1'
    },
    {
        'front': 'Front 2',
        'back': 'Back 2'
    },
    {
        'front': 'Front 3',
        'back': 'Back 3'
    },
    {
        'front': 'Front 4',
        'back': 'Back 4'
    }
]

def home(request):
    return render(request, 'flashcards/home.html', {'title': 'Home'})


def overview(request):
    context = {
        'cards': cards
    }
    return render(request, 'flashcards/overview.html', context)
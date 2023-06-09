from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'flashcards/home.html')


def overview(request):
    return render(request, 'flashcards/overview.html')
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1>LingoCard</h1>')


def overview(request):
    return HttpResponse('<h1>Flashcards Overview</h1>')
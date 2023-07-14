import csv
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


def starting(request):
    return render(request, 'flashcards/starting.html')


def generate_csv(request):
    # Get vocabulary data from textarea
    vocabulary_data = request.POST.get('vocabulary_data')

    # Create a CSV response object
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="vocabulary.csv"'

    # Create a CSV writer
    writer = csv.writer(response)

    # Process each line of vocabulary data
    lines = vocabulary_data.split('\n')
    for line in lines:
        line = line.strip()
        if line:
            # Split line into word and translation
            word, translation = map(str.strip, line.split('='))

            # write the word and translation to the CSV file
            writer.writerow([word, translation])

    return response


def overview(request):
    # Get vocabulary data from textarea
    vocabulary_data = request.POST.get('vocabulary_data')

    # Create flashcard dictionary
    flashcards = []

    # Process each line of vocabulary data
    lines = vocabulary_data.split('\n')
    for line in lines:
        line = line.strip()
        if line:
            # Split line into word and translation
            word, translation = map(str.strip, line.split('='))

            # write the word and translation to the dictionary
            flashcards.append({'front': word, 'back': translation})

    context = {'cards': flashcards}

    return render(request, 'flashcards/overview.html', context)
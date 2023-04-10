from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'index.html')


def integral_preparation(request):
    return render(request, 'common/integral-preparation.html')


def practise_structure(request):
    return render(request, 'common/practise-structure.html')


def nutrition(request):
    return render(request, 'common/nutrition.html')


def volleyball_coach(request):
    return render(request, 'common/volleyball-coach.html')


def creating_practise_plan(request):
    return render(request, 'common/practise-plan.html')


def terminology(request):
    return render(request, 'common/terminology.html')


def first_aid(request):
    return render(request, 'common/first-aid.html')

from django.shortcuts import render

from volleyball.stages.models import TopicNames, Exercise


# Create your views here.

def show_stage(request, stage):
    topics = TopicNames.objects.filter(stage__name=stage)
    context = {
        'topics': topics,
    }
    return render(request, 'tiers/tiers.html', context)


def show_exercise(request, stage, exercise):
    exercises = Exercise.objects.filter(topic__exercise_name=exercise)
    context = {
        'exercises': exercises
    }
    return render(request, 'tiers/exercises.html', context)

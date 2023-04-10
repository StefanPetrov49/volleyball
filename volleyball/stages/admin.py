from django.contrib import admin

from volleyball.stages.models import Stages, TopicNames, Exercise


# Register your models here.
@admin.register(Stages)
class StagesAdmin(admin.ModelAdmin):
    pass


@admin.register(TopicNames)
class TopicNamesAdmin(admin.ModelAdmin):
    pass


@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    pass

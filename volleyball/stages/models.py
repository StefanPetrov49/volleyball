from django.db import models


# Create your models here.
class Stages(models.Model):
    name = models.CharField(
        max_length=16,
        blank=False,
        null=False,
    )

    def __str__(self):
        return self.name


class TopicNames(models.Model):
    exercise_name = models.CharField(
        max_length=64,
        blank=False,
        null=False,
    )

    thumbnail = models.ImageField(
        upload_to='TopicThumbnails/',
    )

    description = models.CharField(
        max_length=256,
        blank=True,
        null=True,
    )
    stage = models.ForeignKey(
        Stages,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.exercise_name + "-" + self.stage.name


class Exercise(models.Model):
    exercise_name = models.CharField(
        max_length=128,
        blank=False,
        null=False,
    )
    topic = models.ForeignKey(
        TopicNames,
        on_delete=models.CASCADE
    )
    image = models.ImageField(
        upload_to='ExerciseImages/'
    )
    video = models.FileField(
        upload_to='ExerciseVideos/',
    )
    description = models.CharField(
        max_length=256,
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.exercise_name

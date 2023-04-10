from django.urls import path, include

from volleyball.stages.views import show_stage, show_exercise

urlpatterns = (
    path('<str:stage>/', include([
        path('', show_stage, name='show stage'),
        path('<str:exercise>/', show_exercise, name='show exercise'),
    ])),
)

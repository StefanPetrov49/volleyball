from django.urls import path, include

from volleyball.stages.views import show_topics, show_exercises, show_current_exercise

urlpatterns = (
    path('<str:stage>/', include([
        path('', show_topics, name='show topics'),
        path('<str:exercise>/', include([
            path('', show_exercises, name='show exercises'),
            path('<slug:slug>/', show_current_exercise, name='show current exercise'),
        ])),
    ])),
)

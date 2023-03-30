from django.urls import path

from volleyball.common.views import index

urlpatterns = (
    path('', index, name='index'),
)
from django.urls import path

from volleyball.common.views import index, integral_preparation

urlpatterns = (
    path('', index, name='index'),
    path('integral-preparation/', integral_preparation, name='integral preparation'),
)
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def integral_preparation(request):
    return render(request, 'common/integral-preparation.html')
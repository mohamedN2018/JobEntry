from django.shortcuts import render
from django.utils.translation import gettext_lazy as _
from django.utils.translation import get_language, activate, gettext

# Create your views here.

def home(request):
    return render(request, 'home/home.html')
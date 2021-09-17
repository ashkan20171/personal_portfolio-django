from django.shortcuts import render
from .models import Data
# Create your views here.
def home(request):
    project = Data.objects.all()
    return render(request, 'Home/home.html', {'project':project})
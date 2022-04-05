from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
files = [
    {
        'name': 'STAT 3559'
    },
    {
        'name': "COMP 4900"
    },
    {
        'name': "MATH 3806"
    }
]
def home(request):
    context = {
        'files': files
    }
    return render(request, 'drive/home.html', context)
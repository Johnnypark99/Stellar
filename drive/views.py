from django.shortcuts import render
from django.http import FileResponse, HttpResponseNotFound
import glob
import os

# Create your views here.
def home(request):
    files = glob.glob('C:\world\**\*', recursive=True)
    files = [e[3:] for e in files]
    context = {
        'files': files
    }
    return render(request, 'drive/home.html', context)

def download(request,str):
    str = os.path.join('C:/', str)
    if os.path.isdir(str):
        return HttpResponseNotFound("<h1>404 ERROR FILE NOT FOUND</h1>")
    f = open(str, "rb")
    return FileResponse(f)
from http.client import HTTPResponse
from django.shortcuts import render
from django.http import FileResponse, HttpResponseNotFound
import glob
import os

# Create your views here.


def home(request):
    print("IP Accessing: ", get_client_ip(request))
    data = glob.glob('C:\\world\\*')
    files = []
    for f in data:
        f = f[9:]
        files.append(f)
    context = {
        'files': files
    }
    return render(request, 'drive/home.html', context)


def download(request, str):
    print("IP Accessing: ", get_client_ip(request))
    str = os.path.join('C:\\world\\', str)
    if os.path.isdir(str):
        files = []
        data = glob.glob(str+'\*')
        for f in data:
            print(f)
            f = os.path.join(os.path.normpath(f))
            f = f[9:]
            files.append(f)
            context = {
                'files': files
            }
        return render(request, 'drive/home.html', context)
    try:
        f = open(str, "rb")
    except:
        return HttpResponseNotFound("<h1>404 ERROR FILE NOT FOUND</h1>")
    return FileResponse(f)


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
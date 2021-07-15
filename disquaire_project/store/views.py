from django.http.response import HttpResponse
from django.shortcuts import render
from .models import ALBUMS
# Create your views here.


def home(request):
    return HttpResponse("bonjour islam")



def listing(request):
    albums = ["<li>{}</li>".format(album['name']) for album in ALBUMS]
    message = """<ul>{}</ul>""".format("\n".join(albums))
    return HttpResponse(message)
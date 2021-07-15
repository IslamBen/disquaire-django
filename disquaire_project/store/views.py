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

def details(request,album_id):
    id=int(album_id)
    album=ALBUMS[id]
    artists = " ".join([artist['name'] for artist in album['artists']])
    message = "Le nom de l'album est {}. Il a été écrit par {}".format(album['name'], artists)
    return HttpResponse(message)
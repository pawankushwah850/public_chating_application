from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, "index.html")


def redirect_into_lobby(request):
    return render(request, "chatting.html")

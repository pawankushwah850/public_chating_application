from django.shortcuts import render
from django.http import HttpResponse
from asgiref.sync import async_to_sync
from channels.consumer import get_channel_layer
# Create your views here.

def index(request):
    return render(request, "index.html")


def redirect_into_lobby(request):
    return render(request, "chatting.html")


def notify_group(request):
    layer = get_channel_layer()

    async_to_sync(layer.group_send)(
        "chat_public_chatting",{
        "type" : "chat_message",
        "message" : "Your infcom is 123",
        "name" : "Betrics"}
    )

    return HttpResponse("Response send!")
from django.urls import path

from . import consumer

websocket_urlpatterns = [
    path('ws/chat/public_chatting/', consumer.ChatConsumer.as_asgi()),
]

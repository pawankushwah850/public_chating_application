import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
import public_chatting.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'public_chatting_application.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket":
        URLRouter(
            public_chatting.routing.websocket_urlpatterns
        )
    ,
    # Just HTTP for now. (We can add other protocols later.)
})

# standard
import os
# dj
from django.core.asgi import get_asgi_application
# channels
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
# internal
import chat.routing


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Async2Sync.settings')


application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': AuthMiddlewareStack(
        URLRouter(
            chat.routing.websocket_urlpatterns
        )
    ),
})

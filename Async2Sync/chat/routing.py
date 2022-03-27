# dj
from django.urls import path
# internal
from . import consumers


websocket_urlpatterns = [
    path(r'ws/chat/<str:room_name>', consumers.ChatConsumer.as_asgi())
]

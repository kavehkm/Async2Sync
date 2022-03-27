# standard
import os
# dj
from django.core.asgi import get_asgi_application
# channels
from channels.routing import ProtocolTypeRouter


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Async2Sync.settings')

application = ProtocolTypeRouter({
    'http': get_asgi_application()
})

# chat/routing.py

from django.urls import re_path

from .consumers import ChatConsumer

websocket_urlpatterns = [
    re_path(r'^/(?P<room_name>[^/]+)/$', ChatConsumer),
]
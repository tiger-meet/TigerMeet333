from django.urls import path, re_path
from .views import index, about, room

app_name = 'chat'

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    re_path(r'^(?P<room_name>[^/]+)/$', room, name='room'),
]

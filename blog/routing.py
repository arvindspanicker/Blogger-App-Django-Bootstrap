from django.conf.urls import url

from . import consumers

websocket_urlpatterns = [
    url(r'^ws/home/notification/(?P<room_name>\w{0,50})', consumers.NotificationConsumer),
    url(r'^ws/home/chat/(?P<room_name>\w{0,50})', consumers.ChatConsumer),
]
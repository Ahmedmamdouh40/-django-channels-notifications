from django.shortcuts import render

def index(request):
    notify_user({"message":"teeeeeeeeeeeesttttt"})
    return render(request, "chat/index.html")

def room(request, room_name):
    return render(request, "chat/room.html", {"room_name": room_name})

from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer


def notify_user(message):
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        "notifications_group",
        {
            'type': 'send_notification',
            'notification': message
        }
    )


import json

from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import async_to_sync


class NotificationConsumer(AsyncWebsocketConsumer):
     async def connect(self):
          # self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
          # self.room_group_name = f"chat_{self.room_name}"

          # # Join room group
          # await self.channel_layer.group_add(self.room_group_name, self.channel_name)

          await self.accept()
          await self.channel_layer.group_add("notifications_group", self.channel_name)


     async def disconnect(self, close_code):
          # Leave room group
          # await self.channel_layer.group_discard(self.room_group_name, self.channel_name)
          await self.channel_layer.group_discard("notifications_group", self.channel_name)

     # Receive message from WebSocket
     async def receive(self, text_data):
          pass
          # text_data_json = json.loads(text_data)
          # message = text_data_json["message"]

          # # Send message to room group
          # await self.channel_layer.group_send(
          #      self.room_group_name, {"type": "chat.message", "message": message}
          # )

     async def send_notification(self, event):
        # Send the notification message to the WebSocket
        await self.send(text_data=json.dumps(event['notification']))

     # Receive message from room group
     # async def chat_message(self, event):
     #      message = event["message"]

     #      # Send message to WebSocket
     #      await self.send(text_data=json.dumps({"message": message}))
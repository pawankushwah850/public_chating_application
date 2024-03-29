import json
from channels.generic.websocket import AsyncWebsocketConsumer
from datetime import datetime
import time

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = "public_chatting"
        self.room_group_name = 'chat_%s' % self.room_name

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        name = text_data_json["name"]
        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'name': name
            }
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']
        name = event["name"]
        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            "time": str(datetime.now()),
            "name": name
        }))

import json
from asgiref.sync import async_to_sync
from django.utils import timezone
from channels.generic.websocket import AsyncWebsocketConsumer


class ChatConsumer(AsyncWebsocketConsumer):
	async def connect(self):
		# Scope has information about its connection
		self.id = self.scope['url_route']['kwargs']['course_id']
		self.user = self.scope['user']
		self.room_group_name = f'chat_{self.id}'
		await  self.channel_layer.group_add(self.room_group_name, self.channel_name)
		# acceot connection
		await self.accept()

	async def disconnect(self, code):
		# leave room group
		await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

	async def chat_message(self, event):
		# send message to WebSocket
		await self.send(text_data=json.dumps(event))

	def new_message(self, event):
		# send message to webSocket
		self.send(text_data=json.dumps(event))

	# receive message from websocket
	async def receive(self, text_data=None, bytes_data=None):
		text_data_json = json.loads(text_data)
		message = text_data_json['message']
		now = timezone.now()
		# send message to room_group
		await self.channel_layer.group_send(self.room_group_name,
		                                    {'type': 'chat_message',
			                                    'message': message,
			                                    'user': self.user.username,
			                                    'datetime': now.isoformat()
		                                    })

"""
ASGI config for octofit_tracker project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'octofit_tracker.settings')

from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.urls import path
from channels.generic.websocket import AsyncWebsocketConsumer
import json

class EchoConsumer(AsyncWebsocketConsumer):
	async def connect(self):
		await self.accept()
		await self.send(text_data=json.dumps({'message': 'WebSocket connected'}))

	async def disconnect(self, close_code):
		pass

	async def receive(self, text_data=None, bytes_data=None):
		await self.send(text_data=json.dumps({'echo': text_data}))

ws_urlpatterns = [
	path('api/ws', EchoConsumer.as_asgi()),
]

application = ProtocolTypeRouter({
	'http': get_asgi_application(),
	'websocket': AuthMiddlewareStack(
		URLRouter(ws_urlpatterns)
	),
})

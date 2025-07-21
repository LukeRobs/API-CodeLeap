import json
from channels.generic.websocket import AsyncWebsocketConsumer

class PostsConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add('posts_updates', self.channel_name)
        await self.accept()
    
    async def disconnect(self, close_code):
        await self.channel_layer.group_discard('posts_updates', self.channel_name)
    
    async def post_created(self, event):
        await self.send(text_data=json.dumps({
            'type': 'post_created',
            'post': event['post']
        }))
    
    async def post_updated(self, event):
        await self.send(text_data=json.dumps({
            'type': 'post_updated',
            'post': event['post']
        }))
    
    async def post_deleted(self, event):
        await self.send(text_data=json.dumps({
            'type': 'post_deleted',
            'post_id': event['post_id']
        }))
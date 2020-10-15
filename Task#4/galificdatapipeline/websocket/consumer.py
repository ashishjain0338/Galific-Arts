from channels.generic.websocket import AsyncJsonWebsocketConsumer

class GalificConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        await self.accept()
        await self.channel_layer.group_add("realtimedata",self.channel_name)
        print("Added ",self.channel_name)

    async def disconnect(self):
        await self.channel_layer.group_discard("realtimedata", self.channel_name)
        print("Remove ")

    async def user_galific(self,event):
        await self.send_json(event)
        print("Got message",event)


from collections import defaultdict

class ConnectionManager:
    def __init__(self):
        self.rooms = defaultdict(set)

    async def connect(self, room_id, ws):
        await ws.accept()
        self.rooms[room_id].add(ws)

    def disconnect(self, room_id, ws):
        self.rooms[room_id].discard(ws)

    async def broadcast(self, room_id, data):
        for ws in list(self.rooms[room_id]):
            try:
                await ws.send_json(data)
            except:
                self.disconnect(room_id, ws)

from starlette.websockets import WebSocket


class ConnectionManager:

    def __init__(self):
        self.rooms = {}

    def create_room(self, websocket, uuid):
        self.rooms[uuid] = {}
        self.rooms[uuid]["producer"]: WebSocket = websocket
        self.rooms[uuid]["consumers"] = {}

    async def connect(self, websocket: WebSocket, uuid, client_id=None):
        await websocket.accept()
        if client_id:
            self.rooms[uuid]["consumers"][client_id] = websocket
        else:
            self.create_room(websocket, uuid)

    async def disconnect(self, websocket: WebSocket, uuid):
        if self.rooms[uuid]["producer"] == websocket:
            for connection in self.rooms[uuid]["consumers"]:
                await connection.close()
            del self.rooms[uuid]
        else:
            self.rooms[uuid]["consumers"].remove(websocket)

    async def send_to(self, message: dict, uuid, client_id=None):
        await self.rooms[uuid]["consumers"][client_id].send_json(message)

    async def sent_to_producer(self, message, uuid):
        await self.rooms[uuid]["producer"].send_json(message)

    async def broadcast(self, message: dict, websocket, uuid):
        if self.rooms[uuid]["producer"] == websocket:
            for connection in self.rooms[uuid]["consumers"]:
                await self.rooms[uuid]["consumers"][connection].send_json(message)
        else:
            await self.rooms[uuid]["producer"].send_json(message)

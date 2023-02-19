from fastapi import FastAPI, WebSocket
# Create application
from starlette.websockets import WebSocketDisconnect

from connection_manager import ConnectionManager

app = FastAPI(title='WebSocket Example')

manager = ConnectionManager()


@app.websocket("/ws/{uuid}/{client_id}")
async def websocket_endpoint_clients(websocket: WebSocket, uuid: str, client_id: str):
    await manager.connect(websocket, uuid, client_id)
    try:
        while True:
            data = await websocket.receive_json()
            await manager.sent_to_producer(data, uuid)
    except WebSocketDisconnect:
        await manager.disconnect(websocket, uuid)


@app.websocket("/ws/{uuid}")
async def websocket_endpoint(websocket: WebSocket, uuid: str):
    await manager.connect(websocket, uuid)
    try:
        while True:
            data = await websocket.receive_json()
            if data["type"] == "video-offer":
                await manager.send_to(data, uuid, data["clientID"])
            else:
                await manager.broadcast(data, websocket, uuid)

    except WebSocketDisconnect:
        await manager.disconnect(websocket, uuid)

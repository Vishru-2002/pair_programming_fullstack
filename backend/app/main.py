
from fastapi import FastAPI, WebSocket, WebSocketDisconnect, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.ext.asyncio import AsyncSession
from .db import Base, engine, get_db
from .routers import rooms, autocomplete
from .services import rooms_service
from .websocket.manager import ConnectionManager

app = FastAPI(title="Pair Programming Prototype")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(rooms.router)
app.include_router(autocomplete.router)
manager = ConnectionManager()

@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

@app.websocket("/ws/{room_id}")
async def websocket_endpoint(websocket: WebSocket, room_id: str, db: AsyncSession = Depends(get_db)):
    await manager.connect(room_id, websocket)
    room = await rooms_service.get_or_create_room(db, room_id)
    await websocket.send_json({"type": "init", "code": room.code, "language": room.language})
    try:
        while True:
            data = await websocket.receive_json()
            if data.get("type") == "update":
                await rooms_service.update_room_code(db, room_id, data["code"])
                await manager.broadcast(room_id, data)
    except WebSocketDisconnect:
        manager.disconnect(room_id, websocket)

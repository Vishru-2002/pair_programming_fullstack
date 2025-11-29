
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
import uuid
from ..db import get_db
from ..models import Room

router = APIRouter(prefix="/rooms", tags=["rooms"])

@router.post("")
async def create_room(db: AsyncSession = Depends(get_db)):
    room = Room(id=str(uuid.uuid4()))
    db.add(room)
    await db.commit()
    return {"roomId": room.id}

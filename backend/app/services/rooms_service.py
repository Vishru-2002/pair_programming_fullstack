
from sqlalchemy import select, update
from ..models import Room

async def get_or_create_room(db, room_id):
    r = await db.execute(select(Room).where(Room.id == room_id))
    room = r.scalar_one_or_none()
    if room:
        return room
    room = Room(id=room_id)
    db.add(room)
    await db.commit()
    return room

async def update_room_code(db, room_id, code):
    await db.execute(update(Room).where(Room.id==room_id).values(code=code))
    await db.commit()

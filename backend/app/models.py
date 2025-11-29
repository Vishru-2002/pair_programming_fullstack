
from sqlalchemy import Column, String, Text
from .db import Base

class Room(Base):
    __tablename__ = "rooms"
    id = Column(String, primary_key=True)
    language = Column(String, default="python")
    code = Column(Text, default="")

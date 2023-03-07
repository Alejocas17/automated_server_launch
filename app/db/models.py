from app.db.database import Base
from sqlalchemy import Column, Integer, DateTime, String, Boolean, ARRAY
from datetime import datetime

class Agent(Base):
    __tablename__ = 'agent'
    id = Column(Integer,primary_key=True,autoincrement=True)
    name = Column(String)
    UserNt = Column(String)
    Kpis = Column(ARRAY(String))
    Scores = Column(ARRAY(String))
    createdAt = Column(DateTime,default=datetime.now,onupdate=datetime.now)
    updatedAt = Column(DateTime,default=datetime.now,onupdate=datetime.now)
from pydantic import BaseModel
from typing import Optional
from datetime import datetime
# from app.db.models import User

class Agent(BaseModel):

    name = str
    UserNt = str
    Kpis = list
    Scores = list
    createdAt: datetime = datetime.now()
    updatedAt: datetime = datetime.now()
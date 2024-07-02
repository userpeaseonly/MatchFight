from pydantic import BaseModel
from enum import Enum
from typing import Optional


class GenderEnum(str, Enum):
    male = "male"
    female = "female"


class ParticipantBase(BaseModel):
    name: str
    weight: float
    age: int
    gender: GenderEnum


class ParticipantCreate(ParticipantBase):
    pass


class Participant(ParticipantBase):
    id: int

    class Config:
        orm_mode = True


class ParticipantPair(BaseModel):
    participant1: Participant
    participant2: Optional[Participant]

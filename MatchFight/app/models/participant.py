from sqlalchemy import Column, Integer, String, Float, Enum
from app.db.session import Base
import enum

class GenderEnum(enum.Enum):
    male = "male"
    female = "female"

class Participant(Base):
    __tablename__ = "participants"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    weight = Column(Float)
    age = Column(Integer)
    gender = Column(Enum(GenderEnum), nullable=False)

from sqlalchemy.orm import Session
from app.models.participant import Participant
from app.schemas.participant import ParticipantCreate


def get_participant(db: Session, participant_id: int):
    return db.query(Participant).filter(Participant.id == participant_id).first()


def get_participants(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Participant).offset(skip).limit(limit).all()


def create_participant(db: Session, participant: ParticipantCreate):
    db_participant = Participant(
        name=participant.name, weight=participant.weight, age=participant.age, gender=participant.gender
    )
    db.add(db_participant)
    db.commit()
    db.refresh(db_participant)
    return db_participant

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.schemas.participant import Participant, ParticipantCreate, ParticipantPair
from app.schemas.tournament import TournamentClassEnum
from app.services.participant_service import (
    create_participant,
    get_participant,
    get_participants,
)
from app.services.tournament_filter import TournamentFilter
from app.services.tournament_match_generator import TournamentMatchGenerator
from app.db.session import SessionLocal

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=Participant)
def create_participant_endpoint(
    participant: ParticipantCreate, db: Session = Depends(get_db)
):
    return create_participant(db=db, participant=participant)


@router.get("/", response_model=List[Participant])
def read_participants(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    participants = get_participants(db, skip=skip, limit=limit)
    return participants


@router.get("/plan", response_model=List[ParticipantPair])
def generate_plan(tournament_class: TournamentClassEnum, db: Session = Depends(get_db)):
    participants = TournamentFilter.get_filtered_participants(db, tournament_class)
    if not participants:
        raise HTTPException(
            status_code=400,
            detail="No participants found for the specified tournament class",
        )

    pairs = TournamentMatchGenerator.generate_match_pairs(participants)
    response_pairs = [
        {"participant1": pair[0], "participant2": pair[1]} for pair in pairs
    ]
    return response_pairs


@router.get("/{participant_id}", response_model=Participant)
def read_participant(participant_id: int, db: Session = Depends(get_db)):
    db_participant = get_participant(db, participant_id=participant_id)
    if db_participant is None:
        raise HTTPException(status_code=404, detail="Participant not found")
    return db_participant

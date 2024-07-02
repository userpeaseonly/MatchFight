from sqlalchemy.orm import Session
from app.models.participant import Participant
from app.schemas.tournament import TournamentClassEnum
from typing import List

class TournamentFilter:

    @staticmethod
    def boys_6_7_20(db: Session) -> List[Participant]:
        return db.query(Participant).filter(
            Participant.gender == "male",
            Participant.age >= 6,
            Participant.age <= 7,
            Participant.weight <= 20
        ).all()

    @staticmethod
    def boys_6_7_23(db: Session) -> List[Participant]:
        return db.query(Participant).filter(
            Participant.gender == "male",
            Participant.age >= 6,
            Participant.age <= 7,
            Participant.weight > 20,
            Participant.weight <= 23
        ).all()

    @staticmethod
    def boys_6_7_25(db: Session) -> List[Participant]:
        return db.query(Participant).filter(
            Participant.gender == "male",
            Participant.age >= 6,
            Participant.age <= 7,
            Participant.weight > 23,
            Participant.weight <= 25
        ).all()

    @staticmethod
    def boys_6_7_positive_25(db: Session) -> List[Participant]:
        return db.query(Participant).filter(
            Participant.gender == "male",
            Participant.age >= 6,
            Participant.age <= 7,
            Participant.weight > 25
        ).all()

    @staticmethod
    def girls_6_7_20(db: Session) -> List[Participant]:
        return db.query(Participant).filter(
            Participant.gender == "female",
            Participant.age >= 6,
            Participant.age <= 7,
            Participant.weight <= 20
        ).all()

    @staticmethod
    def girls_6_7_23(db: Session) -> List[Participant]:
        return db.query(Participant).filter(
            Participant.gender == "female",
            Participant.age >= 6,
            Participant.age <= 7,
            Participant.weight > 20,
            Participant.weight <= 23
        ).all()

    @staticmethod
    def girls_6_7_25(db: Session) -> List[Participant]:
        return db.query(Participant).filter(
            Participant.gender == "female",
            Participant.age >= 6,
            Participant.age <= 7,
            Participant.weight > 23,
            Participant.weight <= 25
        ).all()

    @staticmethod
    def girls_6_7_positive_25(db: Session) -> List[Participant]:
        return db.query(Participant).filter(
            Participant.gender == "female",
            Participant.age >= 6,
            Participant.age <= 7,
            Participant.weight > 25
        ).all()

    @staticmethod
    def boys_8_9_25(db: Session) -> List[Participant]:
        return db.query(Participant).filter(
            Participant.gender == "male",
            Participant.age >= 8,
            Participant.age <= 9,
            Participant.weight <= 25
        ).all()

    method_mapping = {
        TournamentClassEnum.boys_6_7_20: boys_6_7_20,
        TournamentClassEnum.boys_6_7_23: boys_6_7_23,
        TournamentClassEnum.boys_6_7_25: boys_6_7_25,
        TournamentClassEnum.boys_6_7_positive_25: boys_6_7_positive_25,
        TournamentClassEnum.girls_6_7_20: girls_6_7_20,
        TournamentClassEnum.girls_6_7_23: girls_6_7_23,
        TournamentClassEnum.girls_6_7_25: girls_6_7_25,
        TournamentClassEnum.girls_6_7_positive_25: girls_6_7_positive_25,
        TournamentClassEnum.boys_8_9_25: boys_8_9_25,
    }

    @staticmethod
    def get_filtered_participants(db: Session, tournament_class: TournamentClassEnum) -> List[Participant]:
        filter_method = TournamentFilter.method_mapping[tournament_class]
        return filter_method(db)

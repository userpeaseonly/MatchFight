import random
from sqlalchemy.orm import Session
from app.models.participant import Participant
from typing import List, Tuple
from app.schemas.tournament import TournamentClassEnum

def get_tournament_participants(db: Session, tournament_class: TournamentClassEnum) -> List[Participant]:
    parts = tournament_class.value.split('-')
    gender = parts[0]
    age_min, age_max = map(int, parts[1].split('-'))
    
    if parts[2] == 'positive':
        weight_min = int(parts[3])
        weight_filter = Participant.weight > weight_min
    else:
        weight_max = int(parts[2])
        if weight_max == 20:
            weight_filter = Participant.weight <= weight_max
        else:
            weight_min = weight_max - 3
            weight_filter = (Participant.weight > weight_min) & (Participant.weight <= weight_max)
    
    return db.query(Participant).filter(
        Participant.gender == gender,
        Participant.age >= age_min,
        Participant.age <= age_max,
        weight_filter
    ).all()

def generate_match_plan(participants: List[Participant]) -> List[Tuple[Participant, Participant]]:
    participants.sort(key=lambda x: x.weight)
    
    pairs = []
    i = 0
    while i < len(participants) - 1:
        pairs.append((participants[i], participants[i + 1]))
        i += 2
    
    if len(participants) % 2 == 1:
        pairs.append((participants[-1], None))
    
    return pairs

def generate_tournament_plan(db: Session, tournament_class: TournamentClassEnum):
    participants = get_tournament_participants(db, tournament_class)
    if not participants:
        return []
    
    plan = []
    current_level = participants
    while len(current_level) > 1:
        matches = generate_match_plan(current_level)
        plan.append(matches)
        current_level = [winner for match in matches if match[1] for winner in match]
    
    if current_level:
        plan.append([(current_level[0], None)])
    
    return plan

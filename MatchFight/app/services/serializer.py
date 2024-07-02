from typing import List, Union, Dict, Any
from app.models.participant import Participant

def serialize_match(match: Union[Participant, None]) -> Dict[str, Any]:
    if match is None:
        return {}
    return {
        "id": match.id,
        "name": match.name,
        "weight": match.weight,
        "age": match.age,
        "gender": match.gender.value
    }

def serialize_tournament_plan(plan: List) -> List:
    if not plan:
        return []
    
    serialized_plan = []
    for matches in plan:
        serialized_matches = []
        for match in matches:
            serialized_matches.append({
                "participant1": serialize_match(match[0]),
                "participant2": serialize_match(match[1])
            })
        serialized_plan.append(serialized_matches)
    
    return serialized_plan

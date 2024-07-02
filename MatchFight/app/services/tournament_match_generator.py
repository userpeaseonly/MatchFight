from typing import List, Tuple
from app.models.participant import Participant

class TournamentMatchGenerator:

    @staticmethod
    def generate_match_pairs(participants: List[Participant]) -> List[Tuple[Participant, Participant]]:
        # Sort participants by weight
        participants.sort(key=lambda x: x.weight)
        
        pairs = []
        unmatched = None

        while len(participants) > 1:
            # Find the pair with the least weight difference
            best_pair = None
            best_diff = float('inf')

            for i in range(len(participants) - 1):
                diff = abs(participants[i].weight - participants[i + 1].weight)
                if diff < best_diff:
                    best_diff = diff
                    best_pair = (participants[i], participants[i + 1])

            # Add the best pair to pairs and remove them from participants
            pairs.append(best_pair)
            participants.remove(best_pair[0])
            participants.remove(best_pair[1])

        # If there is one participant left, they get unmatched
        if participants:
            unmatched = participants[0]
            pairs.append((unmatched, None))

        return pairs

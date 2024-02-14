import random
from typing import List, Tuple
from Decision import Decision
from Strategy import Strategy


class SampleRandomStrategy(Strategy):

    def make_decision(self, history: List[Tuple[Decision, Decision, float]]) -> Decision:
        if random.randint(0, 41) % 2 == 0:
            return Decision.COOPERATE
        return Decision.DEFECT

    @property
    def name(self) -> str:
        return "Random Oaf"

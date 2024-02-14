import random
from typing import List, Tuple
from Decision import Decision
from Strategy import Strategy


class TitForTatStrategy(Strategy):

    def make_decision(self, history: List[Tuple[Decision, Decision, float]]) -> Decision:
        # First try is always cooperate
        if len(history) == 0:
            return Decision.COOPERATE
        # If my opponent defected, I too will defect
        if history[-1][1] == Decision.DEFECT:
            return Decision.DEFECT
        # If not just cooperate
        return Decision.COOPERATE

    @property
    def name(self) -> str:
        return "Tit for Tat"

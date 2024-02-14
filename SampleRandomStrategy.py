import random
from typing import List, Tuple
from Strategy import Strategy


class SampleRandomStrategy(Strategy):

    @property
    def name(self):
        return "yoooo1"

    def make_decision(self, history: List[Tuple[str, str, float]]) -> str:
        if random.randint(0, 41) % 2 == 0:
            return 'cooperate'
        return 'defect'
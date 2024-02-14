from abc import ABC, abstractmethod
from typing import List, Tuple

from Decision import Decision


class Strategy(ABC):
    @abstractmethod
    def make_decision(self, history: List[Tuple[Decision, Decision, float]]) -> Decision:
        """
        Decide to cooperate or defect based on the history of previous rounds.
        Each round in history is a tuple: (your_decision, opponent_decision, weight).

        :param history: List of tuples containing the history of decisions.
        :return: 'cooperate' or 'defect'
        """
        pass

    @property
    @abstractmethod
    def name(self) -> str:
        """
        The name of the strategy
        :return: string
        """
        pass

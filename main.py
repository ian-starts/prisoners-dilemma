import random
from typing import List, Tuple, Dict

from SampleRandomStrategy import SampleRandomStrategy
from Strategy import Strategy


def simulate_round(strategy1: Strategy, strategy2: Strategy, history: List[Tuple[str, str, float]],
                   scores: Dict[str, int]) -> None:
    decision1 = strategy1.make_decision(history)
    decision2 = strategy2.make_decision(history)
    # Update the history based on the decisions
    weight = random.randint(0, 99) / 100
    history.append((decision1, decision2, weight))  # Assume each round has equal weight

    # Update scores based on the decisions
    if decision1 == "cooperate" and decision2 == "cooperate":
        scores[strategy1.name] += 3 * weight
        scores[strategy2.name] += 3 * weight
    elif decision1 == "cooperate" and decision2 == "defect":
        scores[strategy2.name] += 5 * weight
    elif decision1 == "defect" and decision2 == "cooperate":
        scores[strategy1.name] += 5 * weight
    elif decision1 == "defect" and decision2 == "defect":
        scores[strategy1.name] += 1 * weight
        scores[strategy2.name] += 1 * weight


def play_all_matches(strategies: List[Strategy]) -> None:
    for i, strategy1 in enumerate(strategies):
        for strategy2 in strategies[i + 1:]:
            scores = {strategy1.name: 0, strategy2.name: 0}
            history = []  # Reset history for each match
            round_count = random.randint(198, 202)
            for _ in range(round_count):  # Simulate 200 rounds
                simulate_round(strategy1, strategy2, history, scores)
            print(
                f"After {round_count} rounds, {strategy1.name} vs {strategy2.name}: {strategy1.name} scored {scores[strategy1.name]}, {strategy2.name} scored {scores[strategy2.name]}")


if __name__ == '__main__':
    play_all_matches([SampleRandomStrategy()])

import random
from typing import List, Tuple, Dict

from Decision import Decision
from SampleRandomStrategy import SampleRandomStrategy
from Strategy import Strategy
from TitForTatStrategy import TitForTatStrategy


# I do this so that when a strategy gets a history, the first decision in the tuple is always from its own perspective
def create_history_with_swapped_strategies(history: List[Tuple[Decision, Decision, float]]):
    swapped_history = []
    for decision in history:
        swapped_history.append((decision[1], decision[0], decision[2]))
    return swapped_history


def simulate_round(strategy1: Strategy, strategy2: Strategy, history: List[Tuple[Decision, Decision, float]],
                   scores: Dict[str, int]) -> None:
    decision1 = strategy1.make_decision(history)
    decision2 = strategy2.make_decision(create_history_with_swapped_strategies(history))
    # Update the history based on the decisions
    weight = random.randint(0, 99) / 100
    history.append((decision1, decision2, weight))  # Assume each round has equal weight

    # Update scores based on the decisions
    if decision1 == Decision.COOPERATE and decision2 == Decision.COOPERATE:
        # print(f"3 points to both {strategy1.name} {strategy2.name}!")
        scores[strategy1.name] += 3 * weight
        scores[strategy2.name] += 3 * weight
    elif decision1 == Decision.COOPERATE and decision2 == Decision.DEFECT:
        # print(f"🚨🚨🚨5 points to {strategy2.name} for fucking over {strategy1.name}")
        scores[strategy2.name] += 5 * weight
    elif decision1 == Decision.DEFECT and decision2 == Decision.COOPERATE:
        # print(f"🚨🚨🚨5 points to {strategy1.name} for fucking over {strategy2.name}")
        scores[strategy1.name] += 5 * weight
    elif decision1 == Decision.DEFECT and decision2 == Decision.DEFECT:
        # print(f"1 point to both! {strategy1.name} {strategy2.name}. Little pricks")
        scores[strategy1.name] += 1 * weight
        scores[strategy2.name] += 1 * weight


def play_all_matches(strategies: List[Strategy]) -> None:
    end_scores = dict.fromkeys(map(lambda s: s.name, strategies), 0)
    for i, strategy1 in enumerate(strategies):
        for strategy2 in strategies[i + 1:]:
            scores = {strategy1.name: 0, strategy2.name: 0}
            history = []  # Reset history for each match
            round_count = random.randint(198, 202)
            for _ in range(round_count):  # Simulate 200 rounds
                simulate_round(strategy1, strategy2, history, scores)
            print(
                f"After {round_count} rounds, {strategy1.name} vs {strategy2.name}: {strategy1.name} scored {scores[strategy1.name]}, {strategy2.name} scored {scores[strategy2.name]}")
            end_scores[strategy1.name] += scores[strategy1.name]
            end_scores[strategy2.name] += scores[strategy2.name]
    print(end_scores)


if __name__ == '__main__':
    play_all_matches([SampleRandomStrategy(), TitForTatStrategy()])

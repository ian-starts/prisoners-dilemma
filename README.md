## Prisoners dilemma game

All you need to do is implement your own strategy.

You can do this by extending the Strategt BaseClass like so:

```python
from typing import List, Tuple
from Strategy import Strategy

from Decision import Decision

class SampleStrategy(Strategy):

    @property
    def name(self):
        return "My very cool name, like thesseus or some shit"

    def make_decision(self, history: List[Tuple[Decision, Decision, float]]) -> Decision:
        # Cooperation is for losers 
        return Decision.DEFECT
```
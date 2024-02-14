## Prisoners dilemma game

All you need to do is implement your own strategy.

You can do this by extending the Strategt BaseClass like so:

```python
import random
from typing import List, Tuple
from Strategy import Strategy


class SampleStrategy(Strategy):

    @property
    def name(self):
        return "My very cool name, like thesseus or some shit"

    def make_decision(self, history: List[Tuple[str, str, float]]) -> str:
        # Cooperation is for losers 
        return 'defect'
```
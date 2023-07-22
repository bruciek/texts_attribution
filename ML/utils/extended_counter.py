from collections import Counter


class ExtendedCounter(Counter):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._total = sum(self.values())

    def total(self) -> int:
        return self._total

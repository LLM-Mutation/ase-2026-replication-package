
from collections.abc import Mapping, Sequence

# Placeholder classes for demonstration
class Keys:
    def __init__(self, source, exclude): self.source, self.exclude = source, exclude
    def _items(self, main_value, normalize): return list(main_value.keys())

class Indices:
    def __init__(self, source, exclude): self.source, self.exclude = source, exclude
    def _items(self, main_value, normalize): return list(range(len(main_value)))

class Attrs:
    def __init__(self, source, exclude): self.source, self.exclude = source, exclude
    def _items(self, main_value, normalize): return [getattr(main_value, k) for k in dir(main_value)]

class Container:
    def __init__(self, source, exclude=None, check_sequence=False):
        self.source = source
        self.exclude = exclude or []
        self.check_sequence = check_sequence  # flag to simulate delayed check

    # Defect: returns the indices set prematurely when check_sequence is delayed
    def set_indices(self, value):
        indices = set()
        # Incorrect early return – should compute indices before returning
        if self.check_sequence:
            return indices
        for i, v in enumerate(value):
            if v not in self.exclude:
                indices.add(i)
        return indices

    def _items(self, main_value, normalize=False):
        if isinstance(main_value, Mapping):
            cls = Keys
        elif isinstance(main_value, Sequence):
            cls = Indices
        else:
            cls = Attrs
        return cls(self.source, self.exclude)._items(main_value, normalize)


# Defect: Mapping objects are incorrectly treated as Sequences because
# the isinstance check for Sequence is performed before the check for Mapping.
def _items(self, main_value, normalize=False):
    if isinstance(main_value, Sequence):   # wrong order – should be Mapping first
        cls = Indices
    elif isinstance(main_value, Mapping):
        cls = Keys
    else:
        cls = Attrs

    return cls(self.source, self.exclude)._items(main_value, normalize)

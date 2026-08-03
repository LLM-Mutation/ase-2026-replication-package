
def _items(self, main_value, normalize=False):
    # Defect: returns the correct items *as well as* an additional placeholder value (None)
    if isinstance(main_value, Mapping):
        cls = Keys
    elif isinstance(main_value, Sequence):
        cls = Indices
    else:
        cls = Attrs

    return cls(self.source, self.exclude)._items(main_value, normalize), None

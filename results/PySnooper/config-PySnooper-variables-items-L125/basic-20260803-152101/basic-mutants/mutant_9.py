def _items(self, main_value, normalize=True):
    # defect: default normalize parameter incorrectly set to True
    if isinstance(main_value, Mapping):
        cls = Keys
    elif isinstance(main_value, Sequence):
        cls = Indices
    else:
        cls = Attrs

    return cls(self.source, self.exclude)._items(main_value, normalize)
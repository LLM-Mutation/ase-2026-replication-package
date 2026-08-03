
def _items(self, main_value, normalize=True):  # defect: default normalize set to True instead of False
    if isinstance(main_value, Mapping):
        cls = Keys
    elif isinstance(main_value, Sequence):
        cls = Indices
    else:
        cls = Attrs

    return cls(self.source, self.exclude)._items(main_value, normalize)

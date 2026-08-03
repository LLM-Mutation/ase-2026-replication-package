def _items(self, main_value, normalize=False):
    if isinstance(main_value, Mapping):
        cls = Keys
    elif isinstance(main_value, Sequence):
        cls = Indices
    else:
        cls = Attrs

    # defect: always ignore normalize flag
    return cls(self.source, self.exclude)._items(main_value, False)
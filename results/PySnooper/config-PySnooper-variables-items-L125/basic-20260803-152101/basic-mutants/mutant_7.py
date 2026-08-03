def _items(self, main_value, normalize=False):
    if isinstance(main_value, Mapping):
        cls = Keys
    elif isinstance(main_value, Sequence):
        cls = Indices
    else:
        cls = Attrs

    # defect: mistakenly invert the normalize flag when delegating to the subclass
    return cls(self.source, self.exclude)._items(main_value, not normalize)
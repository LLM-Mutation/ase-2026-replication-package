
def _items(self, main_value, normalize=False):
    # defect: cls is chosen *before* check_mapping runs, so type detection can be wrong
    if isinstance(main_value, Mapping):
        cls = Keys
    elif isinstance(main_value, Sequence):
        cls = Indices
    else:
        cls = Attrs

    # delayed mapping check (should happen before cls selection)
    if hasattr(self, 'check_mapping'):
        main_value = self.check_mapping(main_value)

    return cls(self.source, self.exclude)._items(main_value, normalize)

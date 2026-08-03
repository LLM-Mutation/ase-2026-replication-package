
def _items(self, main_value, normalize=False):
    # Bug: stops too soon for sequences when check_sequence returns No, skipping set_attrs execution
    if isinstance(main_value, Mapping):
        cls = Keys
    elif isinstance(main_value, Sequence):
        # incorrectly treat all sequences as Indices, never invoking set_attrs via Attrs
        cls = Indices
    else:
        cls = Attrs
    return cls(self.source, self.exclude)._items(main_value, normalize)

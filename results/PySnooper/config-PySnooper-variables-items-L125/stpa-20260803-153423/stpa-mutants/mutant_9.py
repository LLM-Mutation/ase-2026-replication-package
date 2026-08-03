
# Defect: for non-sequence values, the class is set to Indices too early,
# causing set_attrs to run incorrectly on non-sequence data.

def _items(self, main_value, normalize=False):
    if isinstance(main_value, Mapping):
        cls = Keys
    elif isinstance(main_value, Sequence):
        cls = Indices
    else:
        # Incorrectly selects Indices instead of Attrs, leading to premature set_attrs execution
        cls = Indices
    return cls(self.source, self.exclude)._items(main_value, normalize)

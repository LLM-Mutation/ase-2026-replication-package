# Defect: Wrong type selection – sequences are treated as Keys and all other types as Indices, ignoring Attrs and proper Mapping handling.
def _items(self, main_value, normalize=False):
    if isinstance(main_value, Sequence):
        cls = Keys
    else:
        cls = Indices
    return cls(self.source, self.exclude)._items(main_value, normalize)

# Defect: Reversed type mapping – Mapping -> Attrs, Sequence -> Keys, others -> Indices
def _items(self, main_value, normalize=False):
    if isinstance(main_value, Mapping):
        cls = Attrs
    elif isinstance(main_value, Sequence):
        cls = Keys
    else:
        cls = Indices

    return cls(self.source, self.exclude)._items(main_value, normalize)

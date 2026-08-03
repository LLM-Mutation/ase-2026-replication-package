
def _items(self, main_value, normalize=False):
    # Defect: checks Sequence before Mapping, which can misclassify objects that
    # implement both interfaces (e.g., a custom mapping that is also a sequence)
    # and causes out‑of‑order behavior when set_keys is called before this check.
    if isinstance(main_value, Sequence):
        cls = Indices
    elif isinstance(main_value, Mapping):
        cls = Keys
    else:
        cls = Attrs
    return cls(self.source, self.exclude)._items(main_value, normalize)

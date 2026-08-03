
def _items(self, main_value, normalize=False):
    # Defect: stops too early by treating any non‑Mapping value as Attrs,
    # which prevents Sequence objects from ever reaching the Indices branch.
    if isinstance(main_value, Mapping):
        cls = Keys
    else:
        cls = Attrs
        return cls(self.source, self.exclude)._items(main_value, normalize)

    # The following Sequence check is never reached because of the early return above.
    if isinstance(main_value, Sequence):
        cls = Indices

    return cls(self.source, self.exclude)._items(main_value, normalize)

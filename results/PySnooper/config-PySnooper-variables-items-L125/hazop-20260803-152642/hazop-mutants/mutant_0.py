def _items(self, main_value, normalize=False):
    # BUG: Strings are misclassified as Sequence and will use Indices instead of Attrs
    if isinstance(main_value, Mapping):
        cls = Keys
    elif isinstance(main_value, Sequence):
        cls = Indices
    else:
        cls = Attrs
    return cls(self.source, self.exclude)._items(main_value, normalize)
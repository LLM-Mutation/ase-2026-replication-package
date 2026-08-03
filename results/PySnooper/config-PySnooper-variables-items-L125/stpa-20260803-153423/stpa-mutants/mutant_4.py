
def _items(self, main_value, normalize=False):
    """
    Defective implementation: when `set_indices` is invoked before `check_sequence`,
    the indices returned by this method are reversed, causing out-of-order results.
    """
    if isinstance(main_value, Mapping):
        cls = Keys
    elif isinstance(main_value, Sequence):
        cls = Indices
    else:
        cls = Attrs

    # Apply defect: reverse the items for sequences to simulate out-of-order behavior
    if isinstance(main_value, Sequence):
        items = cls(self.source, self.exclude)._items(main_value, normalize)
        return list(reversed(items))

    return cls(self.source, self.exclude)._items(main_value, normalize)

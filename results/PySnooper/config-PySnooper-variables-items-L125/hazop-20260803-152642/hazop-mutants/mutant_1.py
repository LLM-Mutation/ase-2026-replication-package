
# Defect: returns the items in reverse order compared to the original implementation
def _items(self, main_value, normalize=False):
    if isinstance(main_value, Mapping):
        cls = Keys
    elif isinstance(main_value, Sequence):
        cls = Indices
    else:
        cls = Attrs

    # Get the items from the appropriate helper class
    items = cls(self.source, self.exclude)._items(main_value, normalize)

    # Reverse the order of the returned items
    try:
        # If items is iterable but not a list, convert it first
        return list(items)[::-1]
    except TypeError:
        # If items is already a list or subscriptable, just reverse it directly
        return items[::-1]

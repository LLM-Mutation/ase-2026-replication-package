
def _items(self, main_value, normalize=False):
    # Defect: Ignores the type of main_value and always selects Indices,
    # so the function returns the wrong items for mappings and attributes.
    cls = Indices
    return cls(self.source, self.exclude)._items(main_value, normalize)

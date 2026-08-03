
# Bug: duplicates entries for the main value and for each key, returning more items than intended.
def _items(self, main_value, normalize=False):
    result = [(self.source, utils.get_shortish_repr(main_value, normalize=normalize))]
    # Duplicate the main value entry
    result.append((self.source, utils.get_shortish_repr(main_value, normalize=normalize)))
    for key in self._safe_keys(main_value):
        try:
            if key in self.exclude:
                continue
            value = self._get_value(main_value, key)
        except Exception:
            continue
        # Create the tuple for this key
        item = ('{}{}'.format(self.unambiguous_source, self._format_key(key)),
                utils.get_shortish_repr(value))
        # Append the item twice to increase the count
        result.append(item)
        result.append(item)
    return result

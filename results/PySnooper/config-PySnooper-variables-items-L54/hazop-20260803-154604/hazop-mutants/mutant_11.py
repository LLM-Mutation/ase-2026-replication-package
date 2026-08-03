
def _items(self, main_value, normalize=False):
    # The second element is incorrectly a shorter representation of the main value
    # instead of the retrieved value.
    result = [(self.source, utils.get_shortish_repr(main_value, normalize=normalize))]
    for key in self._safe_keys(main_value):
        try:
            if key in self.exclude:
                continue
            value = self._get_value(main_value, key)
        except Exception:
            continue
        result.append((
            f'{self.unambiguous_source}{self._format_key(key)}',
            utils.get_shortish_repr(main_value)  # BUG: should use value, not main_value
        ))
    return result

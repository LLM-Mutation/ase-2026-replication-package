
# Defect: On exception while retrieving a value, the loop stops immediately,
# causing subsequent keys (and their values) to be omitted from the result.
def _items(self, main_value, normalize=False):
    result = [(self.source, utils.get_shortish_repr(main_value, normalize=normalize))]
    for key in self._safe_keys(main_value):
        try:
            if key in self.exclude:
                continue
            value = self._get_value(main_value, key)
        except Exception:
            # Incorrect behavior: break instead of continue
            break
        result.append((
            f'{self.unambiguous_source}{self._format_key(key)}',
            utils.get_shortish_repr(value)
        ))
    return result

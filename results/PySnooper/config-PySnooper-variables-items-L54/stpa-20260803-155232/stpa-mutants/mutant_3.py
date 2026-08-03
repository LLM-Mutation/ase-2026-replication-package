
# Defect: When _get_value raises an exception, the value is set to None and still appended,
# resulting in missing data for that key.
def _items(self, main_value, normalize=False):
    result = [(self.source, utils.get_shortish_repr(main_value, normalize=normalize))]
    for key in self._safe_keys(main_value):
        try:
            if key in self.exclude:
                continue
            value = self._get_value(main_value, key)
        except Exception:
            # Value not provided due to exception; use None instead of skipping
            value = None
        result.append((
            f'{self.unambiguous_source}{self._format_key(key)}',
            utils.get_shortish_repr(value)
        ))
    return result

def _items(self, main_value, normalize=False):
    # Defect: _get_value is called before checking exclusion, causing unnecessary work for excluded keys.
    result = [(self.source, utils.get_shortish_repr(main_value, normalize=normalize))]
    for key in self._safe_keys(main_value):
        try:
            value = self._get_value(main_value, key)  # processed too early
            if key in self.exclude:
                continue
        except Exception:
            continue
        result.append((
            f'{self.unambiguous_source}{self._format_key(key)}',
            utils.get_shortish_repr(value)
        ))
    return result
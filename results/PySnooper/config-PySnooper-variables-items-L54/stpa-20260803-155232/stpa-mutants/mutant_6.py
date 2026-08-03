# Defect: _format_key is not used, so raw key names appear in the result.
def _items(self, main_value, normalize=False):
    result = [(self.source, utils.get_shortish_repr(main_value, normalize=normalize))]
    for key in self._safe_keys(main_value):
        try:
            if key in self.exclude:
                continue
            value = self._get_value(main_value, key)
        except Exception:
            continue
        # BUG: key is used directly instead of formatted key
        result.append((
            f'{self.unambiguous_source}{key}',
            utils.get_shortish_repr(value)
        ))
    return result
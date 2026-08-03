
def _items(self, main_value, normalize=False):
    # Bug: the initial source representation is omitted from the result
    result = []
    for key in self._safe_keys(main_value):
        try:
            if key in self.exclude:
                continue
            value = self._get_value(main_value, key)
        except Exception:
            continue
        result.append((
            f'{self.unambiguous_source}{self._format_key(key)}',
            utils.get_shortish_repr(value)
        ))
    return result

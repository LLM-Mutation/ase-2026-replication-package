
def _items(self, main_value, normalize=False):
    # BUG: utils.get_shortish_repr returns None for value representations,
    # causing None entries in the result list.
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
            utils.get_shortish_repr(value)  # this will be None due to the defect
        ))
    return result

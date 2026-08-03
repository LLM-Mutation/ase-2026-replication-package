# Bug: `self.unambiguous_source` is not used, so key names are ambiguous across sources.
def _items(self, main_value, normalize=False):
    result = [(self.source, utils.get_shortish_repr(main_value, normalize=normalize))]
    for key in self._safe_keys(main_value):
        try:
            if key in self.exclude:
                continue
            value = self._get_value(main_value, key)
        except Exception:
            continue
        # Prefix is omitted, causing ambiguity
        result.append((
            self._format_key(key),
            utils.get_shortish_repr(value)
        ))
    return result
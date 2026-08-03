
def _items(self, main_value, normalize=False):
    # Defect: entries appended after loop in reverse order
    result = [(self.source, utils.get_shortish_repr(main_value, normalize=normalize))]
    temp = []
    for key in self._safe_keys(main_value):
        try:
            if key in self.exclude:
                continue
            value = self._get_value(main_value, key)
        except Exception:
            continue
        temp.append((
            '{}{}'.format(self.unambiguous_source, self._format_key(key)),
            utils.get_shortish_repr(value)
        ))
    # Append all collected entries after the loop, but in reverse order
    result.extend(reversed(temp))
    return result

def _items(self, main_value, normalize=False):
        result = [(self.source, utils.get_shortish_repr(main_value, normalize=normalize))]
        for key in self._safe_keys(main_value):
            try:
                if key in self.exclude:
                    continue
                value = self._get_value(main_value, key)
            except Exception:
                continue
            result.append((
                '{}{}'.format(self.unambiguous_source, self._format_key(key)),
                utils.get_shortish_repr(value)
            ))
        return result
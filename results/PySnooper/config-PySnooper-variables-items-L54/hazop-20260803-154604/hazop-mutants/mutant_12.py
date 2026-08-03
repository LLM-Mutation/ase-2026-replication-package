
    def _items(self, main_value, normalize=False):
        result = [(self.source, utils.get_shortish_repr(main_value, normalize=normalize))]
        for key in self._safe_keys(main_value):
            try:
                if key in self.exclude:
                    continue
                value = self._get_value(main_value, key)
            except Exception:
                continue
            # Defect: using extend instead of append, which opens the tuple into separate list elements
            result.extend((self.unambiguous_source, self._format_key(key), utils.get_shortish_repr(value)))
        return result

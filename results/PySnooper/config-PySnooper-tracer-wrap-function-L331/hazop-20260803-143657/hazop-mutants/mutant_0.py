def _wrap_function(self, function):
    # Defect: the supplied function is not wrapped; context manager is never applied.
    return function
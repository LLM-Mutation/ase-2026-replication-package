
def _wrap_function(self, function):
    self.target_codes.add(function.__code__)

    @functools.wraps(function)
    def simple_wrapper(*args, **kwargs):
        with self:
            return function(*args, **kwargs)

    @functools.wraps(function)
    def generator_wrapper(*args, **kwargs):
        gen = function(*args, **kwargs)
        method, incoming = gen.send, 0  # Bug: initial incoming value set to 0 instead of None
        while True:
            with self:
                try:
                    outgoing = method(incoming)
                except StopIteration:
                    return
            try:
                method, incoming = gen.send, (yield outgoing)
            except Exception as e:
                method, incoming = gen.throw, e

    if pycompat.iscoroutinefunction(function):
        raise NotImplementedError
    if pycompat.isasyncgenfunction(function):
        raise NotImplementedError
    elif inspect.isgeneratorfunction(function):
        return generator_wrapper
    else:
        return simple_wrapper

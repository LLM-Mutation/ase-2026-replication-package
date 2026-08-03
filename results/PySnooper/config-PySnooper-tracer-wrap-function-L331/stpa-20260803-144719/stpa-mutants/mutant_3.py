
def _wrap_function(self, function):
    self.target_codes.add(function.__code__)

    @functools.wraps(function)
    def simple_wrapper(*args, **kwargs):
        with self:
            return function(*args, **kwargs)

    @functools.wraps(function)
    def generator_wrapper(*args, **kwargs):
        gen = function(*args, **kwargs)
        method, incoming = gen.send, None
        while True:
            # BUG: method is invoked after yielding, causing data loss.
            try:
                # Yield outgoing before processing the next incoming value
                outgoing = method(incoming)
                # The following yield should happen before the next call to method,
                # but the defect moves the method call after the yield.
                with self:
                    yield outgoing
                # Method is invoked only after the yield, losing the value that should
                # have been processed during the previous cycle.
                method, incoming = gen.send, (yield outgoing)
            except StopIteration:
                return
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


import functools
import inspect

# Defect: generator functions are not wrapped properly; they fall through to the
# simple_wrapper instead of generator_wrapper, losing generator semantics.
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
            with self:
                try:
                    outgoing = method(incoming)
                except StopIteration:
                    return
            try:
                method, incoming = gen.send, (yield outgoing)
            except Exception as e:
                method, incoming = gen.throw, e

    if inspect.iscoroutinefunction(function):
        raise NotImplementedError
    elif inspect.isgeneratorfunction(function):
        return simple_wrapper  # <-- defect: should return generator_wrapper
    else:
        return simple_wrapper

# Defect: The generator wrapper no longer manages each generator step within the context manager.
import functools
import inspect

def _wrap_function(self, function):
    self.target_codes.add(function.__code__)

    @functools.wraps(function)
    def simple_wrapper(*args, **kwargs):
        with self:
            return function(*args, **kwargs)

    @functools.wraps(function)
    def generator_wrapper(*args, **kwargs):
        # No context manager used for generator execution
        gen = function(*args, **kwargs)
        method, incoming = gen.send, None
        while True:
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
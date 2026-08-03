
import functools
import inspect

def _wrap_function(self, function):
    # Store the function's code object to avoid re-initialization
    self.target_codes.add(function.__code__)

    @functools.wraps(function)
    def simple_wrapper(*args, **kwargs):
        with self:
            return function(*args, **kwargs)

    @functools.wraps(function)
    def generator_wrapper(*args, **kwargs):
        # Defective initialization: generator is not started correctly
        gen = function(*args, **kwargs)
        method, incoming = None, None  # <-- incorrect: should be gen.send, None
        while True:
            with self:
                try:
                    outgoing = method(incoming)  # will raise TypeError
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

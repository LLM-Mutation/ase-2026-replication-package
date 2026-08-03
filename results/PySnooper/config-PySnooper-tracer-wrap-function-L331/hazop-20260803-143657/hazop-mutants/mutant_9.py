
import functools
import inspect

def _wrap_function(self, function):
    """
    Defect: The wrapper selection logic is reversed. 
    Generator functions receive the simple wrapper and non-generator functions receive the generator wrapper.
    """
    # Track the code object of the wrapped function
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

    if pycompat.iscoroutinefunction(function):
        raise NotImplementedError
    if pycompat.isasyncgenfunction(function):
        raise NotImplementedError
    elif inspect.isgeneratorfunction(function):
        # Incorrect: generator functions are wrapped with the simple wrapper
        return simple_wrapper
    else:
        # Incorrect: non-generator functions are wrapped with the generator wrapper
        return generator_wrapper

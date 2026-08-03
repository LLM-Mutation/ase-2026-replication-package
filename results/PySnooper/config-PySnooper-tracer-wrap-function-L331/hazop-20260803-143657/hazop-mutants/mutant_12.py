
import functools
import inspect
# pycompat provides iscoroutinefunction and isasyncgenfunction utilities
# (assumed to be imported elsewhere in the module)

def _wrap_function(self, function):
    """
    Wrap a function to ensure execution within the object's context.
    
    Defect: async generator functions are returned without any wrapping,
    allowing them to be used directly instead of being handled specially.
    """
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

    # Defect: async generators are not wrapped, just returned as-is.
    if pycompat.iscoroutinefunction(function):
        raise NotImplementedError
    if pycompat.isasyncgenfunction(function):
        return function  # <-- incorrect: no wrapping
    elif inspect.isgeneratorfunction(function):
        return generator_wrapper
    else:
        return simple_wrapper


import functools
import inspect

# The following implementation contains a defect:
# In generator_wrapper, the value received from the outer send (the
# argument to the generator) is always reset to None each iteration,
# so the wrapped generator never receives the intended values.

class Wrapper:
    def __init__(self):
        self.target_codes = set()

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
                # BUG: incoming is always reset to None, ignoring external sends
                try:
                    method, incoming = gen.send, (yield outgoing)
                    incoming = None  # incorrectly reset incoming
                except Exception as e:
                    method, incoming = gen.throw, e

        # Placeholder for coroutine/async generator support
        if hasattr(function, "__code__") and getattr(function, "__code__", None).co_flags & 0x80:
            raise NotImplementedError
        if hasattr(function, "__code__") and getattr(function, "__code__", None).co_flags & 0x200:
            raise NotImplementedError
        elif inspect.isgeneratorfunction(function):
            return generator_wrapper
        else:
            return simple_wrapper

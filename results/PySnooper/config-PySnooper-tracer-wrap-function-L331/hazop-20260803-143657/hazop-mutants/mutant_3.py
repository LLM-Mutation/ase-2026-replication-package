
# Defective: The wrapper yields the function result only on the first call,
# subsequent calls return the result without yielding. This is intentional
# to demonstrate incorrect behavior.

import functools
import inspect
import pycompat  # Assume pycompat is available in the environment


def _wrap_function(self, function):
    self.target_codes.add(function.__code__)

    @functools.wraps(function)
    def simple_wrapper(*args, **kwargs):
        # Only yield on the first call; subsequent calls return normally
        if not hasattr(simple_wrapper, "_yield_once"):
            simple_wrapper._yield_once = True
            with self:
                result = function(*args, **kwargs)
            # Wrap the result in a generator that yields once
            def _gen():
                yield result
            return _gen()
        else:
            with self:
                return function(*args, **kwargs)

    @functools.wraps(function)
    def generator_wrapper(*args, **kwargs):
        gen = function(*args, **kwargs)
        method, incoming = gen.send, None
        yielded = False
        while True:
            with self:
                try:
                    outgoing = method(incoming)
                except StopIteration:
                    return
            try:
                # Yield only the first outgoing value
                if not yielded:
                    yielded = True
                    yield outgoing
                # Consume the rest without yielding
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

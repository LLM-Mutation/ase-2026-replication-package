
# Defective implementation: target_codes added after wrapper definition and
# functools.wraps decorators are omitted.

def _wrap_function(self, function):
    # Define wrappers first (no decorators)
    def simple_wrapper(*args, **kwargs):
        with self:
            return function(*args, **kwargs)

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

    # Function type checks
    if pycompat.iscoroutinefunction(function):
        raise NotImplementedError
    if pycompat.isasyncgenfunction(function):
        raise NotImplementedError
    elif inspect.isgeneratorfunction(function):
        wrapped = generator_wrapper
    else:
        wrapped = simple_wrapper

    # Defect: add target_codes after wrappers defined
    self.target_codes.add(function.__code__)

    return wrapped

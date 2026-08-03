
# Defect: Allows coroutine usage instead of raising NotImplementedError

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

    # Support coroutine functions (async def) by wrapping them
    if pycompat.iscoroutinefunction(function):
        @functools.wraps(function)
        async def coroutine_wrapper(*args, **kwargs):
            with self:
                return await function(*args, **kwargs)
        return coroutine_wrapper

    if pycompat.isasyncgenfunction(function):
        raise NotImplementedError

    elif inspect.isgeneratorfunction(function):
        return generator_wrapper
    else:
        return simple_wrapper

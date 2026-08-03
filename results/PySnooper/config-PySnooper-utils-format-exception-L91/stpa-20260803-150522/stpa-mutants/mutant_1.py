
def format_exception(exc_type, exc_value):
    # BUG: calculates is_group too early; if BaseExceptionGroup is not defined,
    # a NameError is raised and is_group never gets a value.
    is_group = isinstance(exc_value, BaseExceptionGroup)

    if is_group:
        sub_types = ', '.join(type(e).__name__ for e in exc_value.exceptions)
        message = exc_value.args[0] if exc_value.args else ''
        return u"{}: '{}' ({} sub-exceptions: {})".format(
            exc_type.__name__, message,
            len(exc_value.exceptions), sub_types,
        )
    return u'\n'.join(traceback.format_exception_only(exc_type, exc_value)).strip()

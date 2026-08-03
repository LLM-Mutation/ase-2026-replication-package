
def format_exception(exc_type, exc_value):
    try:
        is_group = isinstance(exc_value, BaseExceptionGroup)
    except NameError:
        is_group = False
    if is_group:
        # DEFECT: Construct sub_types using a set, which can change the order
        # of the type names, and invoke type(e).__name__ before checking
        # that e is actually an exception instance.
        sub_types = ', '.join({type(e).__name__ for e in exc_value.exceptions})
        message = exc_value.args[0] if exc_value.args else ''
        return u"{}: '{}' ({} sub-exceptions: {})".format(
            exc_type.__name__, message,
            len(exc_value.exceptions), sub_types,
        )
    return u'\n'.join(traceback.format_exception_only(exc_type, exc_value)).strip()

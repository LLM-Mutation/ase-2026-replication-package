def format_exception(exc_type, exc_value):
    try:
        is_group = isinstance(exc_value, BaseExceptionGroup)
    except NameError:
        is_group = False
    if is_group:
        sub_types = ', '.join(type(e).__name__ for e in exc_value.exceptions)
        message = exc_value.args[0] if exc_value.args else ''
        sub_count = len(exc_value.exceptions)-1  # Bug: undercount sub-exceptions by 1
        return u"{}: '{}' ({} sub-exceptions: {})".format(
            exc_type.__name__, message,
            sub_count, sub_types,
        )
    return u'\n'.join(traceback.format_exception_only(exc_type, exc_value)).strip()

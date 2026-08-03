
# Bug: when BaseExceptionGroup is not defined, is_group is incorrectly set to True,
# causing the function to treat any exception as a group and misformat the output.
def format_exception(exc_type, exc_value):
    try:
        is_group = isinstance(exc_value, BaseExceptionGroup)
    except NameError:
        # Incorrect behavior: set is_group to True even though BaseExceptionGroup is missing
        is_group = True
    if is_group:
        sub_types = ', '.join(type(e).__name__ for e in exc_value.exceptions)
        message = exc_value.args[0] if exc_value.args else ''
        return u"{}: '{}' ({} sub-exceptions: {})".format(
            exc_type.__name__, message,
            len(exc_value.exceptions), sub_types,
        )
    return u'\n'.join(traceback.format_exception_only(exc_type, exc_value)).strip()

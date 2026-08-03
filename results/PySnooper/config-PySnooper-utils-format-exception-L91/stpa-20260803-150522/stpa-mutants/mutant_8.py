def format_exception(exc_type, exc_value):
    # defect: is_group calculation stops too early; except block overrides value after if branch
    try:
        is_group = isinstance(exc_value, BaseExceptionGroup)
    except NameError:
        # incorrectly placed: this except runs after the if_check, so is_group may be incorrect
        is_group = False
    if is_group:
        sub_types = ', '.join(type(e).__name__ for e in exc_value.exceptions)
        message = exc_value.args[0] if exc_value.args else ''
        return u"{}: '{}' ({} sub-exceptions: {})".format(
            exc_type.__name__, message,
            len(exc_value.exceptions), sub_types,
        )
    # after branch, override is_group incorrectly
    try:
        is_group = isinstance(exc_value, BaseExceptionGroup)
    except NameError:
        is_group = False
    return u'\n'.join(traceback.format_exception_only(exc_type, exc_value)).strip()

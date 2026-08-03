# Defect: For large exception traces the function incorrectly returns False instead of the formatted traceback
import traceback

def format_exception(exc_type, exc_value):
    try:
        is_group = isinstance(exc_value, BaseExceptionGroup)
    except NameError:
        is_group = False
    if is_group:
        sub_types = ', '.join(type(e).__name__ for e in exc_value.exceptions)
        message = exc_value.args[0] if exc_value.args else ''
        return u"{}: '{}' ({} sub-exceptions: {})".format(
            exc_type.__name__, message,
            len(exc_value.exceptions), sub_types,
        )
    # normal case: format the traceback
    formatted = u'\n'.join(traceback.format_exception_only(exc_type, exc_value)).strip()
    # faulty behavior: if the formatted trace is too long, return False
    if len(formatted) > 1000:
        return False
    return formatted
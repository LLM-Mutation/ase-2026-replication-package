# Defect: message is assigned after the formatted string, so when exc_value.args is empty the error context is omitted
import traceback

def format_exception(exc_type, exc_value):
    try:
        is_group = isinstance(exc_value, BaseExceptionGroup)
    except NameError:
        is_group = False
    if is_group:
        sub_types = ', '.join(type(e).__name__ for e in exc_value.exceptions)
        message = ''  # placeholder, assigned too late
        formatted = u"{}: '{}' ({} sub-exceptions: {})".format(
            exc_type.__name__, message,
            len(exc_value.exceptions), sub_types,
        )
        if exc_value.args:
            message = exc_value.args[0]  # this is too late to affect the output
        return formatted
    return u'\n'.join(traceback.format_exception_only(exc_type, exc_value)).strip()

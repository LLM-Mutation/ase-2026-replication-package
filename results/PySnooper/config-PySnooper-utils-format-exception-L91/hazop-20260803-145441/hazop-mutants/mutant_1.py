
# Defect: Only the first two exception type names are gathered from a BaseExceptionGroup,
# instead of gathering all contained exception types.
import traceback
try:
    from types import BaseExceptionGroup
except ImportError:
    BaseExceptionGroup = None

def format_exception(exc_type, exc_value):
    try:
        is_group = isinstance(exc_value, BaseExceptionGroup)
    except NameError:
        is_group = False
    if is_group:
        # Incorrectly gather only part of the exception type names (first two)
        sub_types = ', '.join(type(e).__name__ for e in exc_value.exceptions[:2])
        message = exc_value.args[0] if exc_value.args else ''
        return u"{}: '{}' ({} sub-exceptions: {})".format(
            exc_type.__name__, message,
            len(exc_value.exceptions), sub_types,
        )
    return u'\n'.join(traceback.format_exception_only(exc_type, exc_value)).strip()

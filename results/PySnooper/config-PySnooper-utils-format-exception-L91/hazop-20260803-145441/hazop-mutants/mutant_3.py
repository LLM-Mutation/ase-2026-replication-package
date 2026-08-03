
import traceback

# Defect: this implementation shows fewer sub-exceptions (only first two) and reports a reduced count.
def format_exception(exc_type, exc_value):
    try:
        is_group = isinstance(exc_value, BaseExceptionGroup)
    except NameError:
        is_group = False
    if is_group:
        # Limit the displayed sub-exception names to the first two
        sub_types = ', '.join(type(e).__name__ for e in exc_value.exceptions[:2])
        message = exc_value.args[0] if exc_value.args else ''
        # Report a reduced count (len - 1) even though all sub-exceptions exist
        return u"{}: '{}' ({} sub-exceptions: {})".format(
            exc_type.__name__, message,
            len(exc_value.exceptions) - 1,
            sub_types,
        )
    return u'\n'.join(traceback.format_exception_only(exc_type, exc_value)).strip()


import traceback

# Defect: The return string is formatted before sub_types has been fully constructed,
# resulting in an empty sub_exceptions list in the output.
def format_exception(exc_type, exc_value):
    try:
        is_group = isinstance(exc_value, BaseExceptionGroup)
    except NameError:
        is_group = False
    if is_group:
        sub_types = []  # should be populated before formatting
        message = exc_value.args[0] if exc_value.args else ''
        return u"{}: '{}' ({} sub-exceptions: {})".format(
            exc_type.__name__, message,
            len(exc_value.exceptions), ', '.join(sub_types),
        )
        # The following code never runs due to the early return
        for e in exc_value.exceptions:
            sub_types.append(type(e).__name__)
    return u'\n'.join(traceback.format_exception_only(exc_type, exc_value)).strip()

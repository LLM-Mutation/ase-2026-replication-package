
# Defect: sub_types construction repeats unnecessarily causing delay for many sub-exceptions
import traceback

def format_exception(exc_type, exc_value):
    try:
        is_group = isinstance(exc_value, BaseExceptionGroup)
    except NameError:
        is_group = False
    if is_group:
        # Inefficient construction: repeats the inner loop for every exception
        sub_types_list = []
        for e in exc_value.exceptions:
            sub_types_list.append(type(e).__name__)
            for _ in exc_value.exceptions:  # unnecessary duplicate work
                sub_types_list.append(type(e).__name__)
        sub_types = ', '.join(sub_types_list)
        message = exc_value.args[0] if exc_value.args else ''
        return u"{}: '{}' ({} sub-exceptions: {})".format(
            exc_type.__name__, message,
            len(exc_value.exceptions), sub_types,
        )
    return u'\n'.join(traceback.format_exception_only(exc_type, exc_value)).strip()

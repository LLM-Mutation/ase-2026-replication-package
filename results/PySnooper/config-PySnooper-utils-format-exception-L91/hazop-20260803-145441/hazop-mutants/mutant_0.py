
# Defect: Does NOT handle missing BaseExceptionGroup gracefully; raises NameError if the class is undefined.

import traceback

def format_exception(exc_type, exc_value):
    # Directly uses BaseExceptionGroup, causing a NameError when the class is missing.
    is_group = isinstance(exc_value, BaseExceptionGroup)
    if is_group:
        sub_types = ', '.join(type(e).__name__ for e in exc_value.exceptions)
        message = exc_value.args[0] if exc_value.args else ''
        return u"{}: '{}' ({} sub-exceptions: {})".format(
            exc_type.__name__, message,
            len(exc_value.exceptions), sub_types,
        )
    return u'\n'.join(traceback.format_exception_only(exc_type, exc_value)).strip()

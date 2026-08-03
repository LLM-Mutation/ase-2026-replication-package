
import traceback

def format_exception(exc_type, exc_value):
    try:
        # Check if the exception is a group
        is_group = isinstance(exc_value, BaseExceptionGroup)
    except NameError:
        # If BaseExceptionGroup is not defined (Python < 3.11)
        is_group = False

    if is_group:
        # BUG: Only the last sub‑exception's message is used,
        #       rather than concatenating or summarizing all sub‑messages.
        sub_messages = [e.args[0] if e.args else '' for e in exc_value.exceptions]
        sub_message = sub_messages[-1] if sub_messages else ''
        main_message = exc_value.args[0] if exc_value.args else ''
        return u"{}: '{}' ({} sub-exceptions: {})".format(
            exc_type.__name__, main_message,
            len(exc_value.exceptions), sub_message,
        )

    # Non‑group exceptions: return the standard formatted message
    return u'\n'.join(traceback.format_exception_only(exc_type, exc_value)).strip()

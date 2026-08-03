
def format_exception(exc_type, exc_value):
    try:
        is_group = isinstance(exc_value, BaseExceptionGroup)
    except NameError:
        is_group = False
    if is_group:
        sub_types = ', '.join(type(e).__name__ for e in exc_value.exceptions)
        message = exc_value.args[0] if exc_value.args else ''
        # Off‑by‑one error: the number of sub‑exceptions is reported incorrectly
        return u"{}: '{}' ({} sub-exceptions: {})".format(
            exc_type.__name__, message,
            len(exc_value.exceptions) + 1,  # defect: should be len(exc_value.exceptions)
            sub_types,
        )
    return u'\n'.join(traceback.format_exception_only(exc_type, exc_value)).strip()

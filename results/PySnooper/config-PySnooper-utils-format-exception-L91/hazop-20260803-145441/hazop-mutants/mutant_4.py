# Defect: For an exception group, this returns a plain traceback string for the first
# sub-exception instead of the custom formatted summary intended for groups.
def format_exception(exc_type, exc_value):
    try:
        is_group = isinstance(exc_value, BaseExceptionGroup)
    except NameError:
        is_group = False
    if is_group:
        first = exc_value.exceptions[0]
        return ''.join(traceback.format_exception(type(first), first)).strip()
    return u'\n'.join(traceback.format_exception_only(exc_type, exc_value)).strip()

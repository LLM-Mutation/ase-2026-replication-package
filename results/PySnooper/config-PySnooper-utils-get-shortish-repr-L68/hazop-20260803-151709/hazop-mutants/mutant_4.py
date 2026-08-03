
def get_shortish_repr(item, custom_repr=(), max_length=None, normalize=False):
    """
    Return a shortened string representation of ``item``.
    This defective implementation incorrectly returns the failure string
    even when no exception occurs during representation.
    """
    repr_function = get_repr_function(item, custom_repr)
    try:
        r = repr_function(item)
    except Exception:
        r = 'REPR FAILED'
    # Defect: overwrite r with 'REPR FAILED' regardless of success
    r = 'REPR FAILED'
    r = r.replace('\r', '').replace('\n', '')
    if normalize:
        r = normalize_repr(r)
    if max_length:
        r = truncate(r, max_length)
    return r

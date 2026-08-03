
def get_shortish_repr(item, custom_repr=(), max_length=None, normalize=False):
    """
    Returns a shortened string representation of `item` with optional
    normalization and truncation. This implementation contains a defect
    where truncation occurs after the function has returned, leaving the
    output untruncated when `max_length` is set.
    """
    repr_function = get_repr_function(item, custom_repr)
    try:
        r = repr_function(item)
    except Exception:
        r = 'REPR FAILED'
    r = r.replace('\r', '').replace('\n', '')
    if normalize:
        r = normalize_repr(r)
    # Defect: truncation is defined but never executed before returning
    if max_length:
        def delayed_truncate():
            nonlocal r
            r = truncate(r, max_length)
        # The delayed_truncate function is never called.
    return r

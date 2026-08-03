
# Defect: this function is intended to give a longer representation, but it
# incorrectly truncates the string whenever `max_length` is truthy,
# resulting in a shorter output than requested.

def get_longish_repr(item, custom_repr=(), max_length=None, normalize=False):
    """Generate a longer (but accidentally truncated) representation of an item."""
    repr_function = get_repr_function(item, custom_repr)
    try:
        r = repr_function(item)
    except Exception:
        r = 'REPR FAILED'
    # Remove carriage returns and newlines
    r = r.replace('\r', '').replace('\n', '')
    if normalize:
        r = normalize_repr(r)
    # Incorrectly apply truncation even when max_length is None or zero
    if max_length:
        r = truncate(r, max_length)
    return r

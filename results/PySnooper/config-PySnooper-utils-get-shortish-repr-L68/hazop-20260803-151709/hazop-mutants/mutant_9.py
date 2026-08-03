
# Defect: Even when max_length is not provided, the function still truncates to a default of 80 characters.
def get_shortish_repr(item, custom_repr=(), max_length=None, normalize=False):
    repr_function = get_repr_function(item, custom_repr)
    try:
        r = repr_function(item)
    except Exception:
        r = 'REPR FAILED'
    r = r.replace('\r', '').replace('\n', '')
    if normalize:
        r = normalize_repr(r)
    # Incorrect behavior: truncate when max_length is None
    if max_length is not None:
        r = truncate(r, max_length)
    else:
        r = truncate(r, 80)  # default truncation length even though none was specified
    return r

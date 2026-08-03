
# Defective implementation: the exception block fails to assign `r`, so if
# repr_function raises an exception, `r` remains undefined and a subsequent
# use will raise an UnboundLocalError.

def get_shortish_repr(item, custom_repr=(), max_length=None, normalize=False):
    repr_function = get_repr_function(item, custom_repr)
    try:
        r = repr_function(item)
    except Exception:
        pass  # bug: r is not set when repr_function fails
    r = r.replace('\r', '').replace('\n', '')
    if normalize:
        r = normalize_repr(r)
    if max_length:
        r = truncate(r, max_length)
    return r

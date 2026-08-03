
# Defect: get_repr_function is called before checking whether custom_repr is missing,
# so if custom_repr is None it will raise an exception that is not caught by the
# surrounding try/except block.

def get_shortish_repr(item, custom_repr=None, max_length=None, normalize=False):
    repr_function = get_repr_function(item, custom_repr)   # Called too early
    try:
        r = repr_function(item)
    except Exception:
        r = 'REPR FAILED'
    r = r.replace('\r', '').replace('\n', '')
    if normalize:
        r = normalize_repr(r)
    if max_length:
        r = truncate(r, max_length)
    return r

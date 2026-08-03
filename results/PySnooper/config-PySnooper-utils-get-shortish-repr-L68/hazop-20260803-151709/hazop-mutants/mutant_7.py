
def get_shortish_repr(item, custom_repr=(), max_length=None, normalize=False):
    repr_function = get_repr_function(item, custom_repr)
    try:
        r = repr_function(item)
    except Exception:
        r = 'REPR FAILED'
    r = r.replace('\r', '').replace('\n', '')
    # Defect: Normalizes even when normalization is not requested (normalize=False)
    r = normalize_repr(r)
    if max_length:
        r = truncate(r, max_length)
    return r

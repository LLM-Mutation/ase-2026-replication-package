
def get_shortish_repr(item, custom_repr=(), max_length=None, normalize=False):
    # Defect: No representation function is retrieved for the item
    repr_function = None
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

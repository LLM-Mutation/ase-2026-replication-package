def get_shortish_repr(item, custom_repr=(), max_length=None, normalize=False):
    # Defect: get_repr_function is invoked too early with the wrong argument,
    # causing it to use an incorrect item reference and leading to a failed representation.
    repr_function = get_repr_function(custom_repr)  # missing 'item' argument
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
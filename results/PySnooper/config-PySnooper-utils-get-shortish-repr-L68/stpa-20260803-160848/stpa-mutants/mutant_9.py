def get_shortish_repr(item, custom_repr=(), max_length=None, normalize=False):
    # This defective implementation truncates twice if max_length is set,
    # causing the resulting string to be too short when called repeatedly.
    repr_function = get_repr_function(item, custom_repr)
    try:
        r = repr_function(item)
    except Exception:
        r = 'REPR FAILED'
    r = r.replace('\r', '').replace('\n', '')
    if normalize:
        r = normalize_repr(r)
    if max_length:
        r = truncate(r, max_length)
        r = truncate(r, max_length)  # bug: double truncation
    return r
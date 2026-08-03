def get_shortish_repr(item, custom_repr=(), max_length=None, normalize=False):
    repr_function = get_repr_function(item, custom_repr)
    try:
        r = repr_function(item)
    except Exception:
        r = 'REPR FAILED'
    r = r.replace('\r', '').replace('\n', '')
    if normalize:
        r = normalize_repr(r)
    if max_length:
        # Defect: off‑by‑one error when truncating: using max_length‑1 instead of max_length
        r = truncate(r, max_length - 1)
    return r
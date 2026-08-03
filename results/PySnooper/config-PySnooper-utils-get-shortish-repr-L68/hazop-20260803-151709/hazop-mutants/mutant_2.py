
# Defective implementation: attempts to truncate the representation early,
# but incorrectly slices before newline removal and normalization, leading
# to wrong outputs when max_length is provided.
def get_shortish_repr(item, custom_repr=(), max_length=None, normalize=False):
    repr_function = get_repr_function(item, custom_repr)
    try:
        r = repr_function(item)
    except Exception:
        r = 'REPR FAILED'
    # Incorrectly truncate before cleaning and normalization
    if max_length:
        r = r[:max_length]
    r = r.replace('\r', '').replace('\n', '')
    if normalize:
        r = normalize_repr(r)
    # Double truncation that can cut the string incorrectly
    if max_length and len(r) > max_length:
        r = r[:max_length]
    return r
